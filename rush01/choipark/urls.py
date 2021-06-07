from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.MainView.as_view(), name="main"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('logout/', views.LogOutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('post/', views.AddArticle.as_view(), name="add_article"),
    path('detail/<str:article_id>', views.ArticleView.as_view(),  name="article"),
    path('profile/<int:userid>', views.ProfileView.as_view(),  name="profile"),
]
