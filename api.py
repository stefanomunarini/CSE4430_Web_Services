from bottle import Bottle, run, request, response

from models import CreditCard


app = Bottle()

@app.route('/cc_validity', method='POST')
def check_cc_validity():
    cc_payload = request.forms
    cc = CreditCard(**cc_payload)
    if cc.is_valid():
        response.status=200
        return
    response.status=402
    return

@app.route('/process_payment', method='POST')
def process_payment():
    payload = request.forms
    amount = payload.pop('amount')
    cc = CreditCard(**payload)
    response.status = 200
    return 'Successfully payed {amount}'.format(amount=amount)

run(app, host='localhost', port=8080)
