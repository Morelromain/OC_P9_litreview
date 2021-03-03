from django.forms import forms, ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _

from critique.models import Review
from critique.models import Ticket


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets={
            'body': forms.Textarea(attrs={'cols': 131, 'rows': 5})}
        

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'image']
        widgets={
            'content': forms.Textarea(attrs={'cols': 131, 'rows': 5})}

