import argparse
import json
import requests

from logger import logger
from bs4 import BeautifulSoup


ebay_endpoint_url = 'http://svcs.sandbox.ebay.com/services/search/FindingService/v1?' \
                    'SECURITY-APPNAME=AaltoUni-ws-SBX-3e6eb0ea5-11d466dd&' \
                    'OPERATION-NAME=findItemsByProduct&MESSAGE-PROTOCOL=SOAP12&' \
                    'paginationInput.entriesPerPage=2'

ebay_soap_envelope = '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" ' \
                     'xmlns="http://www.ebay.com/marketplace/search/v1/services">' \
                     '<soap:Header/>' \
                     '<soap:Body>' \
                     '<findItemsByProductRequest>' \
                     '<productId type="{type}">{product_id}</productId>' \
                     '</findItemsByProductRequest>' \
                     '</soap:Body>' \
                     '</soap:Envelope>'


def search_products_by_keyword(keyword):
    isbn = get_isbn_from_goodreads(keyword)
    return get_eBay_products_by_isbn(isbn)


def get_isbn_from_goodreads(keyword):
    logger.info('Searching goodreads.com for keyword {0}'.format(keyword))
    return '0064635481'


def get_eBay_products_by_isbn(isbn):
    logger.info('Searching eBay.com for ISBN {0}'.format(isbn))
    results = []
    for item in _get_response_items('ISBN', isbn):
        result = {'item_id': item.productid.text,
                  'reference_id': item.itemid.text,
                  'title': item.title.text,
                  'price': item.sellingstatus.currentprice.text,
                  'currency': item.sellingstatus.currentprice.attrs['currencyid']}
        results.append(result)

    return results


def get_eBay_product_by_item_id(item_id):
    logger.info('Getting product from eBay.com with item id {0}'.format(item_id))
    try:
        item = _get_response_items('ReferenceID', item_id)[0]
    except IndexError:
        item = []
    return item


def _get_response_items(request_type=None, product_id=None):
    response = _get_soap_response(_get_soap_envelope(request_type, product_id))
    xml = BeautifulSoup(response.text)
    return xml.find_all('item')


def _get_soap_envelope(request_type=None, product_id=None):
    return ebay_soap_envelope.format(type=request_type, product_id=product_id)


def _get_soap_response(envelope):
    return requests.post(ebay_endpoint_url, data=envelope)


def create_parser_arguments():
    parser = argparse.ArgumentParser(description='Search and buy books from eBay.')
    parser.add_argument('-search', metavar='keyword', help='keyword to use for the search')
    parser.add_argument('-buy', metavar='isbn', help='isbn of the product to buy')

    return parser.parse_args()
