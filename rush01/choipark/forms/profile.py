from django import forms
from ..models import UserProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['name', 'surname', 'email', 'description', 'profile_image']
