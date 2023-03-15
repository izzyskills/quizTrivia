from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2']


class ProfileCreationForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['address', 'mobile', 'profile_pic']
