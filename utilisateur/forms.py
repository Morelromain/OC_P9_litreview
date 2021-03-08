from django.forms import ModelForm
from django import forms

from utilisateur.models import User
from utilisateur.models import UserFollows


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name']


class UserFollowsForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['confirm']
