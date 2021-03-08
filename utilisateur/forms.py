from django.forms import ModelForm
from django import forms

from utilisateur.models import User
from utilisateur.models import UserFollows


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={'size': 134}),
            'password': forms.TextInput(attrs={'size': 134}),
            'first_name': forms.TextInput(attrs={'size': 134})
            }
        labels = {
            'username': 'Nom',
            'password': 'Mot de passe',
            'first_name': 'Confirmer mot de passe',
        }
        help_texts = {
            'username': None,
        }


class UserFollowsForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['confirm']
