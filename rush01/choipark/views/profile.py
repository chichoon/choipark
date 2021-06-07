from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import models
from ..forms import ProfileForm
from ..models import UserProfileModel


class ProfileView(FormView):
    template_name = 'profile.html'
    form_class = ProfileForm

    def get(self, request, userid):
        self_flag = 0
        form = self.form_class(initial=self.initial)
        profiles = UserProfileModel.objects.all().filter(username=userid)
        if not profiles:
            UserProfileModel.objects.create(
                username=self.request.user,
                name='',
                surname='',
                email='@',
                description='add description here'
            )
            profiles = UserProfileModel.objects.all().filter(username=userid)
        if self.request.user.id == userid:
            self_flag = 1
        return render(request, self.template_name, {
            'form': form,
            'profiles': profiles[0],
            'if_self': self_flag,
        })
