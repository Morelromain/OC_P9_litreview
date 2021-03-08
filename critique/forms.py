from django import forms

from django.forms import ModelForm
from critique.models import Review
from critique.models import Ticket


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'cols': 131, 'rows': 5}),
            'headline': forms.TextInput(attrs={'size': 134})
            }


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 131, 'rows': 5}),
            'title': forms.TextInput(attrs={'size': 134})
            }
