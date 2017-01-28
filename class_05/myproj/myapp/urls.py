from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.hello),
    url(r'add/$', views.add),

    url(r'temp/$', views.templating),
]