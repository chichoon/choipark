from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import views as auth_views

class LoginView(auth_views.LoginView):
    def get(self, request):
        messages.info(request, "You have successfully login")
        return redirect('')
