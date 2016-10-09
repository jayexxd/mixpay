from paypalrestsdk import *
import logging, random, os, time
from pprint import pprint
os.environ['PAYPAL_MODE'] = "sandbox"
os.environ['PAYPAL_CLIENT_ID'] = "ASUu0Pp7oePCdm2iVehU3ekpnwVaXdvWyPp1wIJ-6jqbgqIrr6dpvpbQawJwVfUvGJd4dpzGaKWR3YWa"
os.environ['PAYPAL_CLIENT_SECRET'] = "EDKkKGae9m4RE6gD8f32Z2V7HgyUcDk__pi6QHq2dPiAbeFy7KZ_RtvW8mwduOENWmUXsiacwNwkqhNg"
logging.basicConfig(level=logging.INFO)

while(1):
    
    amt = random.randint(10,1000)
    payment = Payment({
        "intent": "sale",

     # Payer
        # A resource representing a Payer that funds a payment
        # Use the List of `FundingInstrument` and the Payment Method
        # as 'credit_card'
     "payer": {
         "payment_method": "credit_card",

         # FundingInstrument
         # A resource representing a Payeer's funding instrument.
         # Use a Payer ID (A unique identifier of the payer generated
         # and provided by the facilitator. This is required when
         # creating or using a tokenized funding instrument)
         # and the `CreditCardDetails`
         "funding_instruments": [{

             # CreditCard
             # A resource representing a credit card that can be
             # used to fund a payment.
             "credit_card": {
                 "type": "mastercard",
                 "number": "5421138491640015",
                 "expire_month": "11",
                 "expire_year": "2021",
                 "cvv2": "874",
                 "first_name": "Big Fan Of",
                 "last_name": "MixPay",

                 # Address
                 # Base Address used as shipping or billing
                 # address in a payment. [Optional]
                 "billing_address": {
                     "line1": "NTUitive, 16 Nanyang Dr",
                     "city": "Singapore",
                     "state": "SG",
                     "postal_code": "637722",
                     "country_code": "SG"}}}]},
        # Transaction
        # A transaction defines the contract of a
        # payment - what is the payment for and who
        # is fulfilling it.
     "transactions": [{

         # ItemList
         "item_list": {
             "items": [{
                 "name": "item",
                 "sku": "item",
                 "price": "%d.00" % amt,
                 "currency": "SGD",
                 "quantity": 1}]},

         # Amount
         # Let's you specify a payment amount.
         "amount": {
             "total": "%d.00" % amt,
             "currency": "SGD"},
         "description": "Capitalism hell yeah!"}]})

    # Create Payment and return status( True or False )
    if payment.create():
        pprint(payment)
        print("Payment[%s] created successfully of amount %d" % (payment.id, amt))
    else:
        # Display Error message
        print("Error while creating payment:")
        print(payment.error)
        time.sleep(random.randint(300,900))
