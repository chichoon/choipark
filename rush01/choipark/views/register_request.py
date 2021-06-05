from django.shortcuts import render, redirect
from ..forms import NewUserForm
from django.contrib.auth import login
from django.views.generic import View
from django.contrib import messages


class RegisterView(View):
    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registration successful.")
            return redirect("main")
        messages.error(request, "Unsuccessful registration. Invalid information. ")
        form = NewUserForm
        return render (request, "pages/register.html", context={"register_form":form})
