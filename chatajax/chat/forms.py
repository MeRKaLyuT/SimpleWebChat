from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SendMessage(forms.ModelForm):
    room = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Message
        fields = {
            'message'
        }
        exclude = ['room']
