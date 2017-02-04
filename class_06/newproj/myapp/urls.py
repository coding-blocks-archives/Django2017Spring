from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.hello), # localhost:800/
    url(r'^submit/$', views.submitName), #localhost:8000/submit/
]
