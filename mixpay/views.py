from django.shortcuts import render
import paypalrestsdk
import os
import logging

# set environment variables using fanpu's paypal client account, or alternatively configure before calling
# os.environ['PAYPAL_MODE'] = "sandbox"
# os.environ['PAYPAL_CLIENT_ID'] = "ASUu0Pp7oePCdm2iVehU3ekpnwVaXdvWyPp1wIJ-6jqbgqIrr6dpvpbQawJwVfUvGJd4dpzGaKWR3YWa"
# os.environ['PAYPAL_CLIENT_SECRET'] = "EDKkKGae9m4RE6gD8f32Z2V7HgyUcDk__pi6QHq2dPiAbeFy7KZ_RtvW8mwduOENWmUXsiacwNwkqhNg"

# Create your views here.
def index(request):
    context = {};
    return render(request, 'mixpay/index.html', context)

def settings(request):
    return render(request, 'mixpay/settings.html')

def fanputest(request):
    paypalrestsdk.configure({
        "mode": "sandbox", # sandbox or live
        "client_id": "ASUu0Pp7oePCdm2iVehU3ekpnwVaXdvWyPp1wIJ-6jqbgqIrr6dpvpbQawJwVfUvGJd4dpzGaKWR3YWa",
        "client_secret": "EDKkKGae9m4RE6gD8f32Z2V7HgyUcDk__pi6QHq2dPiAbeFy7KZ_RtvW8mwduOENWmUXsiacwNwkqhNg" })

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "credit_card",
            "funding_instruments": [{
                "credit_card": {
                    "type": "visa",
                    "number": "4417119669820331",
                    "expire_month": "11",
                    "expire_year": "2018",
                    "cvv2": "874",
                    "first_name": "Joe",
                    "last_name": "Shopper" }}]},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": "1.00",
                    "currency": "USD",
                    "quantity": 1 }]},
            "amount": {
                "total": "1.00",
                "currency": "USD" },
            "description": "This is the payment transaction description." }]})

    if payment.create():
        print("Payment created successfully")
    else:
        print(payment.error)
    return render(request, 'mixpay/fanputest.html')

def org(request):
	return render(request, 'mixpay/org.html')

def homepage(request):
    return render(request, 'mixpay/homepage.html')

def login(request):
    return render(request, 'mixpay/login.html')

def register(request):
    return render(request, 'mixpay/register.html')
