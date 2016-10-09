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
    url(r'^org/$', views.org, name="org"),
    url(r'^payments/$', views.payments, name="payments"),
    url(r'^business/$', views.business, name="business"),
    url(r'^business/(?P<org_id>\d+)/$', views.loadbusiness, name="load_business"),
    url(r'^busiess_manage/(?P<org_id>\d+)/$', views.business_manage, name="manage_business"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^personal/$', views.personal, name="personal"),
]
