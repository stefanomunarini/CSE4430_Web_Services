# CSE4430_Web_Services
A basic implementation of a bank web service using Python 3.5.0 and [bottle](http://bottlepy.org)

This web service provide (basic) functionalities to verify credit card validity and process a payment. Therefore, the API endpoints are two:
<ul>
<li>check_cc_validity responsible for verifying the valid of a credit card (mock)</li>
<li>process_payment responsible for processing the payment (mock)</li>
</ul>

The flow is as follow:
<ol>
<li>The client send a request to the web server (check_cc_validity endpoint), including the credit card details in the body of the message</li>
<li>The web server receives the request, checks the validity of the credit card passed with the request and return a response (either positive, status code 200, or negative, status code 402).</li>
<li>The client receive the response. If the status code is 402 it returns, otherwise it add the amount to be payed to the previous payload and send a request to the web server (process_payment endpoint).</li>
<li>The web server receives the request and process the payment returning a status code.</li>
<li>The client receive the response and return the result of the operation</li>
</ol>
