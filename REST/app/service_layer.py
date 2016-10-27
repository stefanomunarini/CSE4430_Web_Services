import requests

from logger import logger
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def _get_ebay_product_infos_by_isbn(isbn):
    logger.info('Searching eBay.com for ISBN {0}'.format(isbn))
    item = _get_response_items('ISBN', isbn)
    if item:
        item = item[0]
        return {'ebay_item_id': item.productid.text,
                'price': item.sellingstatus.currentprice.text,
                'currency': item.sellingstatus.currentprice.attrs['currencyid']
                }
    return None


goodreads_search_books_endpoint_url = 'http://www.goodreads.com/search?q={title}&search_type=books&' \
                                      'key=uv1J3LcJ7zGuhzCXwaCcUQ'


def _search_book_from_goodreads(keyword, number_of_results=10):
    logger.info('Searching goodreads.com for keyword {0}'.format(keyword))
    response = requests.get(goodreads_search_books_endpoint_url.format(title=keyword))
    xml = BeautifulSoup(response.text, "html.parser")
    results = []
    for book in xml.find_all('work')[:number_of_results]:
        result = {
            'goodreads_id': book.id.text,
            'rating': book.average_rating.text,
            'title': book.title.text
        }

        result.update(_get_isbn_from_book_id(book))
        results.append(result)

    return results


def _get_response_items(request_type=None, product_id=None):
    response = _get_soap_response(_get_soap_envelope(request_type, product_id))
    xml = BeautifulSoup(response.text, "html.parser")
    return xml.find_all('item')


ebay_soap_envelope = '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" ' \
                     'xmlns="http://www.ebay.com/marketplace/search/v1/services">' \
                     '<soap:Header/>' \
                     '<soap:Body>' \
                     '<findItemsByProductRequest>' \
                     '<productId type="{type}">{product_id}</productId>' \
                     '</findItemsByProductRequest>' \
                     '</soap:Body>' \
                     '</soap:Envelope>'


def _get_soap_envelope(request_type=None, product_id=None):
    return ebay_soap_envelope.format(type=request_type, product_id=product_id)


ebay_endpoint_url = 'http://svcs.sandbox.ebay.com/services/search/FindingService/v1?' \
                    'SECURITY-APPNAME=AaltoUni-ws-SBX-3e6eb0ea5-11d466dd&' \
                    'OPERATION-NAME=findItemsByProduct&MESSAGE-PROTOCOL=SOAP12&' \
                    'paginationInput.entriesPerPage=10'


def _get_soap_response(envelope):
    return requests.post(ebay_endpoint_url, data=envelope)


goodreads_find_book_endpoint_url = 'https://www.goodreads.com/book/show.xml?id={id}&key=uv1J3LcJ7zGuhzCXwaCcUQ'


def _get_isbn_from_book_id(book):
    response = requests.get(goodreads_find_book_endpoint_url.format(id=book.id.text))
    try:
        root = ET.fromstring(response.text.encode('utf8'))
    except ET.ParseError:
        return {}
    else:
        return {'isbn': root[1][2].text}
