import logging, http

from bottle import Bottle, run, request, response

from models import CreditCard


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Bottle()

@app.route('/cc_validity', method='POST')
def check_cc_validity():
    cc_payload = request.forms
    cc = CreditCard(**cc_payload)
    logger.debug('Checking credit card **** **** **** {last_four_digits} validity.'.format(last_four_digits=cc.cc_number[-4:]))
    if cc.is_valid():
        logger.debug('Valid credit card.')
        response.status = http.client.OK
        return
    logger.debug('Invalid credit card.')
    response.status = http.client.PAYMENT_REQUIRED
    return('Invalid credit card')

@app.route('/process_payment', method='POST')
def process_payment():
    payload = request.forms
    amount = payload.pop('amount')
    cc = CreditCard(**payload)
    logger.debug('Processing payment with card **** **** **** {last_four_digits}. Trying to charge {amount}$.'.format(last_four_digits=cc.cc_number[-4:], amount=amount))
    if(cc.funds_available(amount)):
        logger.debug('Payment approved.')
        response.status = http.client.OK
        return 'Successfully payed {amount}$ with card **** **** **** {last_four_digits}.'.format(last_four_digits=cc.cc_number[-4:], amount=amount)
    logger.debug('Payment denied. Not enough money.')
    response.status = http.client.PAYMENT_REQUIRED
    return('Not enough funds. Please try again with a different credit card!')

run(app, host='localhost', port=8080)
