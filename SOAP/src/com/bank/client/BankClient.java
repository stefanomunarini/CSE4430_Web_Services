package com.bank.client;

import com.bank.models.CreditCard;
import com.bank.ws.WebServerInterface;

import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import java.net.URL;

/**
 * Created by Stefano on 10/5/16.
 */
public class BankClient {

    public static void main(String[] args) throws Exception {

        URL url = new URL("http://localhost:9000/BankWebService?wsdl");
        QName qname = new QName("http://ws.bank.com/", "WebServerService");
        Service service = Service.create(url, qname);
        WebServerInterface wsi = service.getPort(WebServerInterface.class);

        CreditCard cc = new CreditCard();
        cc.setCcNumber(1234567890123456L);
        System.out.println(wsi.checkCcValidity(cc));
    }

}
