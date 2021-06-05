from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import views as auth_views

class LogOutView(auth_views.LogoutView):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        success_url = "login"
