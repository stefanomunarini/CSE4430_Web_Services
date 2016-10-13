import requests

from bottle import Bottle, run, request, response

from settings import WS_ADDRESS, BUSINESS_LAYER_PORT, HOST_ADDRESS

app = Bottle()


@app.route('/', method='POST')
def dispatch():
    request_payload = request.forms
    endpoint = request_payload.pop('endpoint')
    r = requests.post('http://' + WS_ADDRESS + '/{endpoint}'.format(endpoint=endpoint), data=request_payload.dict)
    response.status = r.status_code
    return r.text

run(app, host=HOST_ADDRESS, port=BUSINESS_LAYER_PORT)
