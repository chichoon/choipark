from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.User.as_view(), name="main"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('logout/', views.LogOutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('article', views.ArticleView.as_view(),  name="article"),
]
