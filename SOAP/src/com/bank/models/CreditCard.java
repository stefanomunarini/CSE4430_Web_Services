package com.bank.models;

import java.util.Date;

/**
 * Created by Stefano on 10/5/16.
 */
public class CreditCard {

    private long ccNumber;
    private String ownerFirstName;
    private String ownerLastName;
    private Date expirationDate;
    private int ccv;

    public long getCcNumber() {
        return ccNumber;
    }

    public void setCcNumber(long ccNumber) {
        this.ccNumber = ccNumber;
    }

    public String getOwnerFirstName() {
        return ownerFirstName;
    }

    public void setOwnerFirstName(String ownerFirstName) {
        this.ownerFirstName = ownerFirstName;
    }

    public String getOwnerLastName() {
        return ownerLastName;
    }

    public void setOwnerLastName(String ownerLastName) {
        this.ownerLastName = ownerLastName;
    }

    public Date getExpirationDate() {
        return expirationDate;
    }

    public void setExpirationDate(Date expirationDate) {
        this.expirationDate = expirationDate;
    }

    public int getCcv() {
        return ccv;
    }

    public void setCcv(int ccv) {
        this.ccv = ccv;
    }

    public boolean isValid(){
        return String.valueOf(this.ccNumber).length() == 16;
    }

    public boolean fundsAvailable(int amount) {return (Math.random() < 0.5); }
}
