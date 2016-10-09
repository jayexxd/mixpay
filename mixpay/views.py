from django.shortcuts import render
from paypalrestsdk import *
import os
import logging
from payouts import mixpay_payout # same folder
from pprint import pprint
from userauth.models import UserProfile, User, Organization
import json
from django.http import HttpResponse



logging.basicConfig(level=logging.INFO)

# set environment variables using fanpu's paypal client account, or alternatively configure before calling
os.environ['PAYPAL_MODE'] = "sandbox"
os.environ['PAYPAL_CLIENT_ID'] = "ASUu0Pp7oePCdm2iVehU3ekpnwVaXdvWyPp1wIJ-6jqbgqIrr6dpvpbQawJwVfUvGJd4dpzGaKWR3YWa"
os.environ['PAYPAL_CLIENT_SECRET'] = "EDKkKGae9m4RE6gD8f32Z2V7HgyUcDk__pi6QHq2dPiAbeFy7KZ_RtvW8mwduOENWmUXsiacwNwkqhNg"

# Create your views here.
def index(request):
    context = {};
    return render(request, 'mixpay/index.html', context)

def settings(request):
    return render(request, 'mixpay/settings.html')

def fanputest(request):
    configure({
        "mode": "sandbox", # sandbox or live
        "client_id": "ASUu0Pp7oePCdm2iVehU3ekpnwVaXdvWyPp1wIJ-6jqbgqIrr6dpvpbQawJwVfUvGJd4dpzGaKWR3YWa",
        "client_secret": "EDKkKGae9m4RE6gD8f32Z2V7HgyUcDk__pi6QHq2dPiAbeFy7KZ_RtvW8mwduOENWmUXsiacwNwkqhNg" })
    # payment_list = [{"email" : "mixpay-employee-1@gmail.com", "amount" : "20.00", "note" : "Thank you"}, {"email" : "mixpay-employee-2@gmail.com", "amount" : "65.00", "note" : "Thank you"}, {"email" : "mixpay-employee-3@gmail.com", "amount" : "15.00", "note" : "Thank you"} ]
    payment_list = [{"email" : "dev-null@gmail.com", "amount" : "9110000", "note" : "danke"}]
    obj = json.dumps(payment_list, separators=(',', ': '))
    pprint(obj)
    mixpay_payout(payment_list);
    # payout = Payout.find("PHMMW5XEQSXW4")
    # payout = Payout.find("M3U2WQJQKQBN8")
    # SHH99UV5L3QKW
    # print("Got Details for Payout[%s]" % (payout.batch_header.payout_batch_id))
    # pprint (vars(payout))


    '''
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
    '''
    return render(request, 'mixpay/fanputest.html')


def homepage(request):
    return render(request, 'mixpay/homepage.html')

def login(request):
    return render(request, 'mixpay/login.html')

def register(request):
    return render(request, 'mixpay/register.html')

def sidebar(request):
    return render(request, 'mixpay/sidebar.html')

def org(request):
    context = {}
    # List all organizations that the user belongs to
    print request.user
    def list_organization():
        context["orgs"] = Organization.objects.filter(userprofile= UserProfile.objects.get(user=request.user))
        context["user"] = request.user
    list_organization()
    print context["orgs"]
    return render(request, 'mixpay/org.html', context)

def payments(request):
    context = {}
    context["a_payments"] = True
    return render(request, 'mixpay/payments.html', context)



def business(request):
    context = {}
    # List all organizations that the user belongs to
    def list_organization():
        context["orgs"] = Organization.objects.filter(userprofile= UserProfile.objects.get(user=request.user))
        context["user"] = request.user
    list_organization()
    context["a_business"] = True
    return render(request, 'mixpay/business.html', context)

def loadbusiness(request, org_id):
    context={}
    context["org_id"] = org_id
    return HttpResponse(request, 'mixpay/loadbusiness.html', context)

def business_manage(request, org_id):
    context = {}
    if request.method == "GET":
        context["org"] = Organization.objects.get(id=org_id)
        payment_history = None
        def received_hist():
            payment_history = Payment.all({"count": 3})
            context["payments"] = payment_history
            print payment_history
            print("List Payment:")
            for payment in payment_history.payments:
                print("  -> Payment[%s]" % (payment.id))
        received_hist()
    # return render(request, 'mixpay/business_manage.html', context)
    return HttpResponse(request, 'mixpay/business_manage.html',context)

def dashboard(request):
    context = {}
    context["a_dashboard"] = True
    return render(request, 'mixpay/dashboard.html', context)

def personal(request):
    context = {}
    context["a_personal"] = True
    return render(request, 'mixpay/personal.html', context)
