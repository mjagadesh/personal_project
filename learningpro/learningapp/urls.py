from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
	url('', views.home),
	url('login1/', views.login1),
	url('rest_login/', views.rest_login, name='rest_login',),
]
