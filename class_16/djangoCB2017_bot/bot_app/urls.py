from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^353249793:AAHvZltlXyWwvFj5vRDGGPLq4518npidt7s/', views.hook, name='hook'),
]