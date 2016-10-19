import argparse
import json

import requests

from logger import logger
from settings import BUSINESS_LAYER_ADDRESS

ebay_endpoint_url = 'http://svcs.sandbox.ebay.com/services/search/FindingService/v1?' \
                    'OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&' \
                    'SECURITY-APPNAME=AaltoUni-ws-SBX-3e6eb0ea5-11d466dd&RESPONSE-DATA-FORMAT=JSON&' \
                    'SOAP-PAYLOAD&paginationInput.entriesPerPage=5&productId.@type={type}&productId={product_id}'


def get_info(keyword):
    logger.info('Searching goodreads.com for keyword {0}'.format(keyword))
    # isbn = goodreadserapi.getisbn()
    results = get_eBay_products_by_isbn('0023805811')
    if not results:
        return ['Unable to find any book with \'{}\' keyword. Try using a different keyword'.format(keyword)]

    return results


def get_eBay_products_by_isbn(isbn):
    logger.info('Searching eBay.com for ISBN {0}'.format(isbn))
    response = requests.get(ebay_endpoint_url.format(type='ISBN', product_id=isbn))
    data = json.loads(response.text)
    results = []

    for elem in data['findItemsByProductResponse'][0]['searchResult'][0]['item']:
        result = {'item_id': elem['productId'][0]['__value__'],
                  'title': elem['title'][0],
                  'price': elem['sellingStatus'][0]['currentPrice'][0]['__value__'],
                  'currency': elem['sellingStatus'][0]['currentPrice'][0]['@currencyId']}
        results.append(result)

    return results


def buy_product(cc_number, item_id):
    logger.info('Buying item {0} from eBay.com'.format(item_id))
    product = get_eBay_product_by_item_id(item_id)
    payload = {'cc_number': cc_number, 'endpoint': 'process_payment',
               'amount': product['sellingStatus'][0]['currentPrice'][0]['__value__']}
    r = requests.post('http://' + BUSINESS_LAYER_ADDRESS, data=payload)

    return r.text


def get_eBay_product_by_item_id(item_id):
    logger.info('Getting product from eBay.com with item id {0}'.format(item_id))
    response = requests.get(ebay_endpoint_url.format(type='ReferenceID', product_id=item_id))
    data = json.loads(response.text)
    return data['findItemsByProductResponse'][0]['searchResult'][0]['item'][0]


def create_parser_arguments():
    parser = argparse.ArgumentParser(description='Search and buy books from eBay.')
    parser.add_argument('-search', metavar='keyword', help='keyword to use for the search')
    parser.add_argument('-buy', metavar='isbn', help='isbn of the product to buy')

    return parser.parse_args()
