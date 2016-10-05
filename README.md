# Web Services 
https://mycourses.aalto.fi/course/info.php?id=13068

Basic REST and SOAP implementations of a bank service. The REST web service was implemented with Python 3.5.0 and [bottle](http://bottlepy.org) and the SOAP with Java 8.

### Endpoints

This web service provide (basic) functionalities to verify credit card validity and process a payment. Therefore, the API endpoints are two:
<ul>
<li>check_cc_validity responsible for verifying the valid of a credit card (mock)</li>
<li>process_payment responsible for processing the payment (mock)</li>
</ul>

### Flow
The flow is as follow:
<ol>
<li>The client send a request to the web server (check_cc_validity endpoint), including the credit card details in the body of the message</li>
<li>The web server receives the request, checks the validity of the credit card passed with the request and return a response (either positive, status code 200, or negative, status code 402).</li>
<li>The client receive the response and checks the status code: if it is 402 it returns, otherwise it adds the amount to be payed to the previous payload and it sends a request to the web server (process_payment endpoint).</li>
<li>The web server receives the request and process the payment.</li>
<li>The client receive the response and returns the result of the operation.</li>
</ol>

## REST
### Usage

Create a virtualenv

`mkvirtualenv rest_ws`

If it is the first time that this environment is created, go to the next step. Otherwise, activate the environment

`workon rest_ws`

Install all the requirements

`pip install -r requirements`

You are now ready to start the webserver

`python ws.py`

and the test client

`python client.py`

By default the number of the credit card used for testing is 16 digits long (required condition for the web service to consider the credit card valid). It is possible to use a different number, in order to test the endpoints, passing it as an argument when starting the client

`python client.py 12345`
