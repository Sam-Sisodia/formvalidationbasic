from django.contrib import admin
from django.urls import path,include
from Basic import views

urlpatterns = [
    path('',views.home),
    path('register',views.register , name= "register")

]