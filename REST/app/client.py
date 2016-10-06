import requests, sys

from models import CreditCard


amount = 10
valid_message = 'Your payment has been processed. {amount}$ has been transfer to the seller. You will receive your item soon!'
invalid_credit_card = 'Invalid credit card'
something_went_wrong = 'Ops! Something went wrong.'

def test_bank_service(cc_number):
    cc = CreditCard(cc_number, 'Stefano', 'Munarini', '12/16', '123')
    payload = cc.__dict__
    r = requests.post('http://localhost:8080/cc_validity', data=payload)
    if (r.status_code != 200):
        return invalid_credit_card 
    payload['amount'] = amount
    r = requests.post('http://localhost:8080/process_payment', data=payload)
    if (r.status_code == 200):
        return r.text
    else:
        return r.text

if __name__ == '__main__':
    cc_number = 1234567890123456
    args = sys.argv
    if (len(args)>1):
        cc_number = args[1]
    print(test_bank_service(cc_number))
