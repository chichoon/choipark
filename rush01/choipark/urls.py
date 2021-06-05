from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('tip', views.createtip.as_view(),  name="tip"),
]
