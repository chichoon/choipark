from django.shortcuts import render, redirect
from django.views.generic import CreateView 
from ..forms import NewUserForm
from django.contrib.auth import login
from django.views.generic import View
from django.contrib import messages


class RegisterView(CreateView):
    form_class = NewUserForm
    template_name = 'registration/register.html'
    success_url = "login"