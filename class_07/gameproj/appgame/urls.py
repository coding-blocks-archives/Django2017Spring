from django.conf.urls import url
import views

urlpatterns = [
    url(r'^testing/', views.testing),
    url(r'^$', views.home),
    url(r'^game/', views.playGame),
    url(r'^gamescore/', views.gameScore),
    url(r'^leaderboard/', views.leaderBoard),
    url(r'^mypage/', views.myPage),
]