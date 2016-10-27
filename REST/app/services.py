from logger import logger
from service_layer import _search_book_from_goodreads, _get_ebay_product_infos_by_isbn, _get_response_items


def get_products_by_keyword(keyword):
    books = _search_book_from_goodreads(keyword)
    for book in books:
        if not book.get('isbn'):
            """
            If no results are returned, go to http://books.shop.sandbox.ebay.com/
            pick a book and update the below isbn (ISBN-10)
            """
            book['isbn'] = '1465420274'
        ebay_product = _get_ebay_product_infos_by_isbn(book.get('isbn'))
        if not ebay_product:
            books.remove(book)
        else:
            book.update(ebay_product)
    return books


def get_ebay_product_by_item_id(item_id):
    logger.info('Getting product from eBay.com with item id {0}'.format(item_id))
    try:
        item = _get_response_items('ReferenceID', item_id)[0]
    except IndexError:
        item = []
        logger.error('No item returned from eBay search with id {}'.format(item_id))
    return item
