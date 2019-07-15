# coding=utf-8
"""
author: xiaorui
date: 2019-07-14 12:18
"""
from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.course_index, name='course_index'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
]
