from django.forms import forms, ModelForm

from utilisateur.models import User
from utilisateur.models import UserFollows


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserFollowsForm(ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']