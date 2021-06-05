from django import forms


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    email = forms.EmailField()
    description = forms.CharField()
    profile_image = forms.ImageField()
