from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^sidebar/$', views.sidebar, name='sidebar'),
    url(r'^settings/$', views.settings, name="settings"),
    url(r'^auth/', include('userauth.urls')),
    url(r'^fanputest/$', views.fanputest),
    url(r'^org/$', views.org, name="org")

]
