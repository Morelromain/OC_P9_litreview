from django.forms import forms, ModelForm
from django import forms

from utilisateur.models import User
from utilisateur.models import UserFollows


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name']

class UserFollowsForm(ModelForm):
    #followed_user = forms.CharField
    class Meta:
        model = UserFollows
        fields = ['followed_user']
        #widgets = {'followed_user': forms.TextInput}
    #def clean_followed_user(self):
    #    followed_user = self.cleaned_data.get("clean_followed_user")
    #    return followed_user