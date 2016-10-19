import requests

from pysimplesoap.client import SoapClient
from bottle import Bottle, run, request, response

from settings import WS_ADDRESS, BUSINESS_LAYER_PORT, HOST_ADDRESS
from services import get_info

app = Bottle()
client = SoapClient('http://demo.seco.tkk.fi/ws/5/?wsdl')


@app.route('/', method='POST')
def dispatch():
    request_payload = request.forms
    endpoint = request_payload.pop('endpoint')

    if endpoint == 'search_product':
        keyword = request_payload.pop('keyword')
        return get_info(keyword)
    elif endpoint == 'process_payment':
        r = requests.post('http://' + WS_ADDRESS + '/cc_validity', data=request_payload.dict)
        if r.status_code != 402:
            r = requests.post('http://' + WS_ADDRESS + '/process_payment', data=request_payload.dict)
            response.status = r.status_code
        return r.text
    else:
        response.status = 404
        return None


run(app, host=HOST_ADDRESS, port=BUSINESS_LAYER_PORT)
