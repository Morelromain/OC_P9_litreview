from django.forms import forms, ModelForm

from utilisateur.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
