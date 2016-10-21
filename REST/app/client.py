import requests

from termcolor import colored

import services
from settings import BUSINESS_LAYER_ADDRESS

cc_number = 1234567890123456
arg = services.create_parser_arguments()


payload = {'cc_number': cc_number}

keyword = arg.search
if keyword:
    payload['endpoint'] = 'search_product'
    payload['keyword'] = keyword

item_id = arg.buy
if item_id:
    payload['endpoint'] = 'process_payment'
    payload['item_id'] = item_id

if payload.get('endpoint'):
    response = requests.post('http://' + BUSINESS_LAYER_ADDRESS, data=payload)
    if response.status_code != 500:
        if response.status_code in (402, 403):
            print(colored(response.text, 'red'))
        else:
            print(colored(response.text, 'green'))
    else:
        print(colored('Ops. Something went wrong!', 'red'))
else:
    print(colored('You need to provide an option when executing the script. To get the list of available commands'
          'type \'python client.py -h\'.', 'red'))

# args = sys.argv
# if len(args) > 1:
#     cc_number = args[1]
# if len(args) > 2:
#     amount = args[2]
# print(test_bank_service(cc_number, amount))
