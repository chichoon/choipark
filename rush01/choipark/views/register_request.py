from django.views.generic import CreateView
from ..forms import NewUserForm


class RegisterView(CreateView):
    form_class = NewUserForm
    template_name = 'registration/register.html'
    success_url = "login"
