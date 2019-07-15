# coding=utf-8
"""
author: xiaorui
date: 2019-07-14 10:38
"""
from django.urls import path
from . import views

app_name = 'xfzzuth'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='logout'),
    path('img_captcha/', views.img_captcha, name='img_captcha'),
]
