<<<<<<< HEAD
"""mixpay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
=======
from django.conf.urls import include, url
>>>>>>> 36d40d538d9c9b1c228028b39e82c529f57ceaac
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='index'),
<<<<<<< HEAD
    url(r'^login/$', views.login, name='login'),
    url(r'^sidebar/$', views.sidebar, name='sidebar'),
    url(r'^settings/$', views.settings, name="settings"),
=======
    url(r'^settings/$', views.settings, name="settings"),
    url(r'^auth/', include('userauth.urls')),
    url(r'^fanputest/$', views.fanputest),
>>>>>>> 36d40d538d9c9b1c228028b39e82c529f57ceaac

]
