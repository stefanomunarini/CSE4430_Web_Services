# Bank Web Service 
https://mycourses.aalto.fi/course/info.php?id=13068


The practical assignment for the course is to plan and implement a programmatic book seller web service that hooks into web services provided by eBay and Goodreads. Product information and user ratings for the books are sourced through the REST API of Goodreads, while product offers are fetched from eBay. Payment is handled by "third party” bank web services, in reality also developed as part of the exercise. Finally, to test the book seller web service, a front-end client is created.

The point of the exercise is to learn how to use and deploy web services. Thus, the actual front-end itself does not need to be anything special. It can be a Javascript enabled web page, or even a text mode program run from the command line. In a similar fashion, the bank service developed don't actually have to do anything sensible (e.g. security checks or balance keeping), but just appear to do so when called from the web.

In the practical assignment, the following high-level functionality is to be implemented:
<ul>
<li>The user can search for books using a keyword search</li>
<li>The search is passed to Goodreads. Additional information about the matched books is also sourced from Goodreads</li> <li>Available offers for the books on the other hand are sourced from eBay</li>
<li>After looking at the books and reviews returned via keyword search, the user selects some books to buy</li>
<li>The books can be paid through two different third party banks, one created by you and another created by another course participant</li>
<li>After a successful payment, the shop acknowledges the order as successful</li>
</ul>

### Development Progress

At the moment, only the REST and the SOAP bank web services, that provide functionalities to process the payment, have been implemented. In addition, a client for testing purposes has been implemented.

### Technologies

The REST web service was implemented with Python 3.5.0 and [bottle](http://bottlepy.org) while the SOAP with Java7.

### Endpoints

The API endpoints of the web services are:
<ul>
<li><i>check_cc_validity</i> responsible for verifying the validity of a credit card (mock)</li>
<li><i>process_payment</i> responsible for processing the payment (mock)</li>
</ul>
