from django.shortcuts import render
from paypalrestsdk import *
import os
import logging
from payouts import mixpay_payout # same folder
from pprint import pprint
from userauth.models import UserProfile, User, Organization, PayoutSetting
import json, copy
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

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

def help(request):
    return render(request, 'mixpay/help.html')

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


@login_required
def business(request):
    context = {}
    # List all organizations that the user belongs to
    context["orgs"] = context["orgs"] = Organization.objects.filter(userprofile= UserProfile.objects.get(user=request.user)) # DO NOT TOUCH CODE WITH CORNER CASES YOU DON'T UNDERSTAND
    context["user"] = request.user
    context["a_business"] = True
    return render(request, 'mixpay/business.html', context)

def business_manage(request, org_id):
    context = {}
    context["org"] = Organization.objects.get(id=org_id)
    payment_history = None
    def received_hist():
        num_count = 20
        total = 0
        payment_history = Payment.all({"count": num_count})
        context["payments"] = payment_history
        time_data = []
        price_data = []
        for payment in payment_history.payments:
            time_data.append(payment["update_time"])
            price_data.append(payment["transactions"][0]["amount"]["total"])
            total += float(payment["transactions"][0]["amount"]["total"])
            # payment["transactions"][0]["amount"]["total"]
        context["time_data"] = json.dumps(time_data)
        context["price_data"] = json.dumps(price_data)
        context["total"] = total
        context["average"] = total/num_count

    def getOrgMembers():
        return UserProfile.objects.filter(organization=org_id)
    context["members"] = getOrgMembers()
    context["num_members"] = len(context["members"])
    received_hist()
    context["a_business"] = True

    def getPayoutInfo():
        context["setting"] = PayoutSetting.objects.get_or_create(organization=Organization.objects.get(id=org_id))
    getPayoutInfo()
    print context["setting"]
    return render(request, 'mixpay/business_manage.html',context)

def dashboard(request):
    context = {}
    context["a_dashboard"] = True
    payment_history = None
    def received_hist():
        num_count = 20
        total = 0
        payment_history = Payment.all({"count": num_count})
        time_data = []
        price_data = []
        for payment in payment_history.payments:
            time_data.append(payment["update_time"])
            price_data.append(payment["transactions"][0]["amount"]["total"])
            payment["transactions"][0]["amount"]["total"] *= 1
            total += float(payment["transactions"][0]["amount"]["total"])           
        context["payments"] = payment_history
        context["time_data"] = json.dumps(time_data)
        context["price_data"] = json.dumps(price_data)
        context["total"] = total
        context["average"] = total/num_count
    received_hist()
    return render(request, 'mixpay/dashboard.html', context)

def personal(request):
    context = {}
    context["a_personal"] = True
    payment_history = None
    def received_hist():
        num_count = 20
        total = 0
        payment_history = Payment.all({"count": num_count})
        time_data = []
        price_data = []
        for payment in payment_history.payments:
            time_data.append(payment["update_time"])
            price_data.append(payment["transactions"][0]["amount"]["total"])
            payment["transactions"][0]["amount"]["total"] *= 1
            total += float(payment["transactions"][0]["amount"]["total"])           
        context["payments"] = payment_history
        context["time_data"] = json.dumps(time_data)
        context["price_data"] = json.dumps(price_data)
        context["total"] = total
        context["average"] = total/num_count
    received_hist()
    return render(request, 'mixpay/personal.html', context)
