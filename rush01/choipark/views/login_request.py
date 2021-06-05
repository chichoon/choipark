from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
class LoginView(View):
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_vaild():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main")
            else :
                messages.error(request, "Invalid username or password.")
        else :
            messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request, "pages/login.html", {"login_form" : form})
