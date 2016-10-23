##REST
### Usage

Create a virtualenv

`mkvirtualenv rest_ws`

Activate the environment

`workon rest_ws`

Install all the requirements

`pip install -r requirements`

You are now ready to start the webserver

`python ws.py`

and the test client

`python client.py -search 'keyword'`

The other client options are:

`-buy 'ebay_item_id'` allows to purchase a particular item, after collecting the id from the search
`-po 'payment_option[0-1]'` allows to select which of the payment methods available to use (0 default, 1 third party)
