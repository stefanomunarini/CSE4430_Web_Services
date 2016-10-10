package com.bank.client;


/**
 * Created by Stefano on 10/5/16.
 */
public class BankClient {

    public static void main(String[] args) throws Exception {

        WebServerService webServerService = new WebServerService();
        WebServerInterface webServerInterface = webServerService.getWebServerPort();

        CreditCard cc = new CreditCard();
        cc.setCcNumber(1234567890123456L);

        int responseStatusCode = webServerInterface.checkCcValidity(cc);
        if (responseStatusCode==200){
            System.out.println("Valid credit card.");
        } else {
            System.out.println("Invalid credit card.");
            return;
        }

        responseStatusCode = webServerInterface.processPayment(cc, 10);
        if (responseStatusCode == 200){
            System.out.println("Payment approved.");
        } else {
            System.out.println("Payment denied, not enough fund.");
        }
    }

}
