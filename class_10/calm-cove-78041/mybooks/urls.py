from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.hello, name='home'),
    url(r'^main/$', views.main, name='main'),
    url(r'^submitform/$', views.MyView.as_view(), name='submitform'),
    url(r'^page/(?P<pr>\d+)/$', views.count),
    url(r'^magic/$', views.magic, name='magic'),
    url(r'^news/$', views.populate_news, name='news'),
    url(r'^shownews/$', views.show_news, name='shownews'),
]