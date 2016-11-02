# Online Book Shop
https://mycourses.aalto.fi/course/info.php?id=13068

This accademic project aim at providing a platform in where users can search for books, get their information and reviews (through Goodreads APIs), get their prices (through eBay APIs) and finally select and buy some of them.

### Project Requirements 

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

### Architecture

The project is a mix of REST and SOAP web services.

A REST web service is responsible for the business logic of the app. Every requests sent to this web server (`/REST/app/business_layer.py`) is forwarded to the appropriate web service (eBay, Goodreads or Bank). The Bank Web Service  has been implemented both as a REST WS `/REST/app/ws.py` and as a SOAP WS `/SOAP/src/com/bank/ws/WebServer.java`.

### Technologies

The REST web service was implemented with Python 3.5.0 and [bottle](http://bottlepy.org) while the SOAP with Java7.

### Testing

For information about how to test the project please refer to [this](https://github.com/stefanomunarini/CSE4430_Web_Services/blob/master/REST/README.md) README.

### Limitations

Due to the use of the ebay sandbox, many search results won't have any price and ebay_item_id. This is because the ebay sandbox database is very little populated, therefore lot of information are missing.
