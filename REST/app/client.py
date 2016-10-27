import argparse
import os
import requests

from termcolor import colored

from settings import BUSINESS_LAYER_ADDRESS

cc_number = 1234567890123456

parser = argparse.ArgumentParser(description='Search and buy books from eBay.')
parser.add_argument('-search', metavar='[keyword]', help='keyword to use for the search')
parser.add_argument('-buy', metavar='[isbn]', help='isbn of the product to buy')
parser.add_argument('-po', metavar='[0-1]{1}', type=int,
                    help='choose a different payment method (0 default / 1 third party')
args = parser.parse_args()

payload = {'cc_number': cc_number,
           'payment_option': 0}

keyword = args.search
if keyword:
    payload['endpoint'] = 'search_product'
    payload['keyword'] = keyword

item_id = args.buy
if item_id:
    payload['endpoint'] = 'process_payment'
    payload['ebay_item_id'] = item_id

payment_option = args.po
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
