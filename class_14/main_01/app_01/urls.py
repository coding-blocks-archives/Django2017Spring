from django.conf.urls import url, include
import app_01.views as views

urlpatterns = [
    url(r'^$', views.main, name='home'),
    url(r'^about/$', views.about, name='about'),
]
