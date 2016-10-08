from django.shortcuts import render

# Create your views here.
def index(request):
    context = {};
    return render(request, 'mixpay/index.html', context)

def settings(request):
    return render(request, 'mixpay/settings.html')

def fanputest(request):
    return render(request, 'mixpay/fanputest.html')

def homepage(request):
    return render(request, 'mixpay/homepage.html')

def login(request):
    return render(request, 'mixpay/login.html')

def register(request):
    return render(request, 'mixpay/register.html')

def sidebar(request):
    return render(request, 'mixpay/sidebar.html')
