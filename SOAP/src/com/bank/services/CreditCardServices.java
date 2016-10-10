package com.bank.services;

import com.bank.client.CreditCard;

/**
 * Created by Stefano on 10/10/16.
 */
public class CreditCardServices {

    public static boolean isValid(CreditCard creditCard){
        return String.valueOf(creditCard.getCcNumber()).length() == 16;
    }

    public static boolean fundsAvailable(int amount) {return (Math.random() < 0.5); }
}
