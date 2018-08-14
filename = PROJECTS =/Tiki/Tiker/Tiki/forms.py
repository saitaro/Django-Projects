from django.forms import ModelForm, DateTimeField
from .models import Ticket
from django.db import models
from django.contrib.admin import widgets
from django import forms

class TicketForm(ModelForm):
    # task = forms.CharField()
    # date = forms.DateTimeField(widget=forms.DateTimeField())

    class Meta:
        model = Ticket
        fields = ('task',)
        