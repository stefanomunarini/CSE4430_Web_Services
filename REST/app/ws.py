import http

from bottle import Bottle, run, request, response

from models import CreditCard
from logger import logger
from settings import WS_PORT, HOST_ADDRESS

app = Bottle()


@app.route('/cc_validity', method='POST')
def check_cc_validity():
    payload = request.forms
    cc = CreditCard(**payload)
    logger.info(
        'Checking credit card **** **** **** {last_four_digits} validity.'.format(last_four_digits=cc['cc_number'][-4:]))
    if cc.is_valid():
        logger.info('Valid credit card.')
        response.status = http.client.OK
        return
    logger.info('Invalid credit card.')
    response.status = http.client.PAYMENT_REQUIRED

    return 'Invalid credit card'


@app.route('/process_payment', method='POST')
def process_payment():
    payload = request.forms
    amount = payload.pop('amount')
    cc = CreditCard(**payload)
    logger.info('Processing payment with card **** **** **** {last_four_digits}. Charging {amount}$.'.format(
        last_four_digits=cc['cc_number'][-4:], amount=amount))
    if cc.funds_available(amount):
        logger.info('Payment approved.')
        response.status = http.client.OK
        return 'Successfully payed {amount}$ with card **** **** **** {last_four_digits}.'.format(
            last_four_digits=cc['cc_number'][-4:], amount=amount)
    logger.error('Payment denied. Not enough money.')
    response.status = http.client.PAYMENT_REQUIRED

    return 'Not enough funds. Please try again with a different credit card!'


run(app, host=HOST_ADDRESS, port=WS_PORT)
