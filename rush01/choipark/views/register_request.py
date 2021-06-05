from django.shortcuts import render, redirect
from django.views.generic import CreateView 
from ..forms import NewUserForm
from django.contrib.auth import login
from django.views.generic import View
from django.contrib import messages


class RegisterView(CreateView):
    form_class = NewUserForm
    template_name = 'pages/register.html'
    success_rul = "/"
#     def post(self, request):
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             messages.success(request, "Registration successful.")
#             return redirect("main")
#         messages.error(request, "Unsuccessful registration. Invalid information. ")
#         form = NewUserForm
#         return render (request, "pages/register.html", context={"register_form":form})




# class UserCreateView(CreateView): #2
#     form_class = UserForm 
#     template_name = 'reviewBoard/signup.html'
#     success_url = "/" #1