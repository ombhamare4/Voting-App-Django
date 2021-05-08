from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('top',views.top,name="top"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('about',views.top,name="about"),
    path('add_poll',views.add_poll,name="add_poll"),
    path('list_poll',views.list_poll,name="list_poll"),
    path('vote_poll/<poll_id>/',views.vote_poll,name="vote_poll"),
    path('result_poll/<poll_id>/',views.result_poll,name="result_poll"),
]
