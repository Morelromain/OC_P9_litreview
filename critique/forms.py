from django.forms import forms, ModelForm

from critique.models import Review
from critique.models import Ticket


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['image', 'title', 'content']

