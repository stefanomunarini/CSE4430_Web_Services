import json
import requests

from bottle import Bottle, run, request, response

from services import get_ebay_product_by_item_id, get_products_by_keyword
from settings import WS_ADDRESS, BUSINESS_LAYER_PORT, HOST_ADDRESS


app = Bottle()

third_party_payment_params = {"amountInCents": 0,
                              "card": {
                                  "owner": 'Test',
                                  "number": '4123456789019999',
                                  "validYear": 2018,
                                  "validMonth": 12,
                                  "csv": 123
                              },
                              "targetIBAN": 123456789,
                              "transactionMessage": 'Payment'
                              }


@app.route('/', method='POST')
def dispatch():
    request_payload = request.forms
    endpoint = request_payload.pop('endpoint')

    if endpoint == 'search_product':
        keyword = request_payload.pop('keyword')
        return json.dumps(get_products_by_keyword(keyword))
    elif endpoint == 'process_payment':
        item_id = request_payload['ebay_item_id']
        product = get_ebay_product_by_item_id(item_id)
        if product:
            price = product.sellingstatus.currentprice.text
            if request_payload.get('payment_option') == '1':
                third_party_payment_params['amountInCents'] = float(price)*100
                r = requests.post('http://demo.seco.tkk.fi/ws/6/t755300bank/', params=third_party_payment_params)
                if r.status_code == 200:
                    return 'Successfully payed {amount}$ with card **** **** **** {last_four_digits}.'.format(
                        last_four_digits=third_party_payment_params['card']['number'][-4:], amount=price)
                return 'Payment denied!'
            else:
                request_payload['amount'] = price
                r = requests.post('http://' + WS_ADDRESS + '/cc_validity', data=request_payload.dict)
                if r.status_code != 402:
                    r = requests.post('http://' + WS_ADDRESS + '/process_payment', data=request_payload.dict)
                    response.status = r.status_code
            return r.text
        else:
            response.status = 403
            return 'Invalid item id!'
    else:
        response.status = 404
        return 'Endpoint not found!'


run(app, host=HOST_ADDRESS, port=BUSINESS_LAYER_PORT)
