import json

import requests

from pysimplesoap.client import SoapClient
from bottle import Bottle, run, request, response

from services import get_eBay_product_by_item_id, get_products_by_keyword
from settings import WS_ADDRESS, BUSINESS_LAYER_PORT, HOST_ADDRESS

app = Bottle()
client = SoapClient('http://demo.seco.tkk.fi/ws/5/')



@app.route('/', method='POST')
def dispatch():
    request_payload = request.forms
    endpoint = request_payload.pop('endpoint')

    if endpoint == 'search_product':
        keyword = request_payload.pop('keyword')
        results = request_payload.get('results', 5)
        return json.dumps(get_products_by_keyword(keyword, results))
    elif endpoint == 'process_payment':
        item_id = request_payload['ebay_item_id']
        product = get_eBay_product_by_item_id(item_id)
        if product:
            request_payload['amount'] = product.sellingstatus.currentprice.text
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
