from django.shortcuts import render
import urllib2


# Create your views here.
def index(request):
    context = {};
    return render(request, 'mixpay/index.html', context)

def settings(request):
    return render(request, 'mixpay/settings.html')

def fanputest(request):
    return render(request, 'mixpay/fanputest.html')
