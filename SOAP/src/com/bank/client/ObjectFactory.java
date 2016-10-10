
package com.bank.client;

import javax.xml.bind.JAXBElement;
import javax.xml.bind.annotation.XmlElementDecl;
import javax.xml.bind.annotation.XmlRegistry;
import javax.xml.namespace.QName;


/**
 * This object contains factory methods for each 
 * Java content interface and Java element interface 
 * generated in the com.bank.client package. 
 * <p>An ObjectFactory allows you to programatically 
 * construct new instances of the Java representation 
 * for XML content. The Java representation of XML 
 * content can consist of schema derived interfaces 
 * and classes representing the binding of schema 
 * type definitions, element declarations and model 
 * groups.  Factory methods for each of these are 
 * provided in this class.
 * 
 */
@XmlRegistry
public class ObjectFactory {

    private final static QName _ProcessPayment_QNAME = new QName("http://ws.bank.com/", "processPayment");
    private final static QName _CheckCcValidity_QNAME = new QName("http://ws.bank.com/", "checkCcValidity");
    private final static QName _CheckCcValidityResponse_QNAME = new QName("http://ws.bank.com/", "checkCcValidityResponse");
    private final static QName _ProcessPaymentResponse_QNAME = new QName("http://ws.bank.com/", "processPaymentResponse");

    /**
     * Create a new ObjectFactory that can be used to create new instances of schema derived classes for package: com.bank.client
     * 
     */
    public ObjectFactory() {
    }

    /**
     * Create an instance of {@link ProcessPayment }
     * 
     */
    public ProcessPayment createProcessPayment() {
        return new ProcessPayment();
    }

    /**
     * Create an instance of {@link CheckCcValidity }
     * 
     */
    public CheckCcValidity createCheckCcValidity() {
        return new CheckCcValidity();
    }

    /**
     * Create an instance of {@link CheckCcValidityResponse }
     * 
     */
    public CheckCcValidityResponse createCheckCcValidityResponse() {
        return new CheckCcValidityResponse();
    }

    /**
     * Create an instance of {@link ProcessPaymentResponse }
     * 
     */
    public ProcessPaymentResponse createProcessPaymentResponse() {
        return new ProcessPaymentResponse();
    }

    /**
     * Create an instance of {@link CreditCard }
     * 
     */
    public CreditCard createCreditCard() {
        return new CreditCard();
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link ProcessPayment }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://ws.bank.com/", name = "processPayment")
    public JAXBElement<ProcessPayment> createProcessPayment(ProcessPayment value) {
        return new JAXBElement<ProcessPayment>(_ProcessPayment_QNAME, ProcessPayment.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link CheckCcValidity }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://ws.bank.com/", name = "checkCcValidity")
    public JAXBElement<CheckCcValidity> createCheckCcValidity(CheckCcValidity value) {
        return new JAXBElement<CheckCcValidity>(_CheckCcValidity_QNAME, CheckCcValidity.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link CheckCcValidityResponse }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://ws.bank.com/", name = "checkCcValidityResponse")
    public JAXBElement<CheckCcValidityResponse> createCheckCcValidityResponse(CheckCcValidityResponse value) {
        return new JAXBElement<CheckCcValidityResponse>(_CheckCcValidityResponse_QNAME, CheckCcValidityResponse.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link ProcessPaymentResponse }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://ws.bank.com/", name = "processPaymentResponse")
    public JAXBElement<ProcessPaymentResponse> createProcessPaymentResponse(ProcessPaymentResponse value) {
        return new JAXBElement<ProcessPaymentResponse>(_ProcessPaymentResponse_QNAME, ProcessPaymentResponse.class, null, value);
    }

}
