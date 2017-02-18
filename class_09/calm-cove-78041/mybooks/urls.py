from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.hello),
    url(r'^main/$', views.main),
    url(r'^submitform/$', views.MyView.as_view()),
    url(r'^page/(?P<pr>\d+)/$', views.count),
    url(r'^magic/$', views.magic),
    url(r'^news/$', views.populate_news),
]