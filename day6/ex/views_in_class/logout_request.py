from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib import messages


class LogOutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("main")
