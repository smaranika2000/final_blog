from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),  
    path('about1',views.about1,name="about1"), 
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('upload', views.upload, name="upload"),

    path('one',views.one,name="one"),
    path('two',views.two,name="two"),
    path('three',views.three,name="three"),
    path('four',views.four,name="four"),
    path('own',views.own,name="own"),

    path('appointment',views.appointment,name="appointment"),
    

]
