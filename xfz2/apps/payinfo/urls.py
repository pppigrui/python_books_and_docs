# coding=utf-8
"""
author: xiaorui
date: 2019-07-14 12:38
"""
from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.payinfo, name='payinfo'),
]
