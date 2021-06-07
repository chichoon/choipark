from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

class LoginView(LoginRequiredMixin, auth_views.LoginView):
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('login')

    def get(self, request):
        messages.info(request, "You have successfully login")
        return redirect('main')
