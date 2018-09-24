from django import forms
from django.core import validators
from .custom_validators import *

class QuoteForm(forms.Form):

    name = forms.CharField(label='Nome', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Seu Nome'}))

    email = forms.EmailField(label='E-mail', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'email@email.com'}))

    consumo = forms.CharField(label='Consumo (kWh)', required=True,
                                widget=forms.TextInput(attrs={'placeholder': '200'}),
                                validators=[check_kwh])

    cep = forms.CharField(label='CEP', max_length=9, required=True,
                widget=forms.TextInput(attrs={'placeholder': '12345-678'}),
                validators=[check_cep])

    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
