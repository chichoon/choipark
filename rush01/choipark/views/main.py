from django.shortcuts import render, redirect
from django.views.generic import CreateView 
from ..forms import NewUserForm
from django.contrib.auth import login
from django.views.generic import View
from django.contrib import messages


class MainView(View):
    def get(self, request) :
        template_name = 'base.html'
        return(render(request, 'base.html'))
