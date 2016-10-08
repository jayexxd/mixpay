from django.conf.urls import url
import views

app_name = 'auth'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^profile/(?P<profile_id>\d+)/$', views.profile, name='profile'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^edit/$', views.user_edit, name='edit_profile'),
    url(r'^settings/$', views.user_settings, name='edit_settings')
]
