from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.hello, name='home'),
    url(r'^api/$', views.apicall, name='api'),
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^userlogin/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^regsubmit/$', views.register_data, name='register_data'),
]
