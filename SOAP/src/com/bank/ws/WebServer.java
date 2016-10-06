package com.bank.ws;

import com.bank.models.CreditCard;

import javax.jws.WebService;

@WebService(endpointInterface = "com.bank.ws.WebServerInterface")
public class WebServer implements WebServerInterface{

    @Override
    public int checkCcValidity(CreditCard creditCard) {
        if(creditCard.isValid()){
            return 200;
        }
        return 402;
    }

    @Override
    public int processPayment(CreditCard creditCard, int amount) {
        if (creditCard.fundsAvailable(amount)){
            return 200;
        }
        return 402;
    }
}