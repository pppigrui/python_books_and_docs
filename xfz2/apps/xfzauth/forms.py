# coding=utf-8
"""
author: xiaorui
date: 2019-07-14 03:22
"""

from django import forms
from apps.forms import FormBase


class LoginForm(forms.Form, FormBase):
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20, min_length=6,
                               error_messages={"max_length": "密码最多不能超过20个字符", "min_length": "密码不能少于6个字符"})
    remember = forms.IntegerField(required=False)
