from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.User.as_view(), name="main"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('login', views.LoginView.as_view(), name="login"),
    path('logout', views.LogOutView.as_view(), name="logout"),
    path('tip', views.TipView.as_view(),  name="tip"),
]
