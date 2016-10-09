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

`python client.py`

By default the number of the credit card used for testing is 16 digits long (required condition for the web service to consider the credit card valid). It is possible to use a different number, in order to test the endpoints, passing it as an argument when starting the client

`python client.py 12345`

You can also customize the amount to be payed, passing a second parameter when starting the client:

`python client.py 1234567890123456 20`
