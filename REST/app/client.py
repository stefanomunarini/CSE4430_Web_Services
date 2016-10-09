import requests, sys


def test_bank_service(cc_number, amount):
    payload = {'cc_number': cc_number}
    r = requests.post('http://localhost:8080/cc_validity', data=payload)
    if r.status_code != 200:
        return r.text 
    payload['amount'] = amount
    r = requests.post('http://localhost:8080/process_payment', data=payload)
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
