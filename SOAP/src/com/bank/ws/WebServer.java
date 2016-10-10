package com.bank.ws;

import com.bank.client.CreditCard;
import com.bank.services.CreditCardServices;

import javax.jws.WebService;

@WebService(endpointInterface = "com.bank.ws.WebServerInterface")
public class WebServer implements WebServerInterface{

    @Override
    public int checkCcValidity(CreditCard creditCard) {
        if(CreditCardServices.isValid(creditCard)){
            return 200;
        }
        return 402;
    }

    @Override
    public int processPayment(CreditCard creditCard, int amount) {
        if (CreditCardServices.fundsAvailable(amount)){
            return 200;
        }
        return 402;
    }
}