import os

import requests

from termcolor import colored

import services
from settings import BUSINESS_LAYER_ADDRESS

cc_number = 1234567890123456
arg = services.create_parser_arguments()


payload = {'cc_number': cc_number,
           'payment_option': 0}

keyword = arg.search
if keyword:
    payload['endpoint'] = 'search_product'
    payload['keyword'] = keyword

item_id = arg.buy
if item_id:
    payload['endpoint'] = 'process_payment'
    payload['ebay_item_id'] = item_id

payment_option = arg.po
if payment_option:
    payload['payment_option'] = payment_option

if payload.get('endpoint'):
    response = requests.post('http://' + BUSINESS_LAYER_ADDRESS, data=payload)
    if response.status_code != 500:
        if response.status_code in (402, 403):
            print(colored(response.text, 'red'))
        else:
            if item_id:
                print(colored(response.text, 'green'))
            else:
                for item in response.json():
                    print(colored(item, 'green'))
                    print('\n')

    else:
        print(colored('Ops. Something went wrong!', 'red'))
else:
    os.system('python client.py -h')
