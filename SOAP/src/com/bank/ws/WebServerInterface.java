
package com.bank.ws;

import com.bank.client.CreditCard;

import javax.jws.WebMethod;
import javax.jws.WebService;

/**
 * Created by Stefano on 10/5/16.
 */
@WebService
public interface WebServerInterface {

    @WebMethod int checkCcValidity(CreditCard creditCard);
    @WebMethod int processPayment(CreditCard creditCard, int amount);


}
