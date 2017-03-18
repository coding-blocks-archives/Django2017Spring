from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.main, name='home'),
    url(r'^about/$', views.about, name='about'),
]
