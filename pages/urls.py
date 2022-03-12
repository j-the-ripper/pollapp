#!/usr/bin/env python3


from django.urls import path, include
from . import views

app_name = "pages"
urlpatterns = [
    path('', views.index, name='index'),
]
