from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^org/', views.org, name='index'),
    url(r'^$', views.homepage, name='index'),
    url(r'^settings/$', views.settings, name="settings"),
    url(r'^auth/', include('userauth.urls')),
    url(r'^fanputest/$', views.fanputest),

]
