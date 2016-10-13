import requests, sys

from settings import BUSINESS_LAYER_ADDRESS


def test_bank_service(cc_number, amount):
    payload = {'cc_number': cc_number, 'endpoint': 'cc_validity'}
    r = requests.post('http://' + BUSINESS_LAYER_ADDRESS, data=payload)
    if r.status_code != 200:
        return r.text
    payload['amount'] = amount
    payload['endpoint'] = 'process_payment'
    r = requests.post('http://' + BUSINESS_LAYER_ADDRESS, data=payload)
    return r.text

cc_number = 1234567890123456
amount = 10

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        cc_number = args[1]
    if len(args) > 2:
        amount = args[2]
    print(test_bank_service(cc_number, amount))
