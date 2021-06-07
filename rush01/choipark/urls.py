from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.MainView.as_view(), name="main"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('logout/', views.LogOutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('post/', views.AddArticle.as_view(), name="add_article"),
    path('detail/<int:article_id>', views.ArticleView.as_view(),  name="article"),
    path('detail/<int:comment_id>', views.CreateComment.as_view(),  name="detail"),
    path('profile/<int:userid>', views.ProfileView.as_view(),  name="profile"),
    path('profile/modify', views.ProfileModifyView.as_view(),  name="modify_profile"),
]
