from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', unique=True)
    name = models.CharField('name', max_length=30)
    surname = models.CharField('surname', max_length=30)
    email = models.EmailField('email', unique=True)
    description = models.TextField('description')
    profile_image = models.ImageField('profile_image')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'
