package com.bank.ws;

import javax.xml.ws.Endpoint;

/**
 * Created by Stefano on 10/5/16.
 */
public class WebServerPublisher {

    public static void main(String[] argv) {
        Endpoint.publish("http://localhost:9000/BankWebService", new WebServer());
    }

}
