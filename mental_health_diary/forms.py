from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Entry
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EntryForm(forms.ModelForm):
    happiness = forms.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(5)],
                                   help_text="Please enter your happiness from -5 to 5.",
                                   widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                   'placeholder': '-5 - 5',
                                                                   'min': -5,
                                                                   'max': 5}))

    disgust = forms.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(5)],
                                 help_text="Please enter your disgust from -5 to 5.",
                                 widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                 'placeholder': '-5 - 5',
                                                                 'min': -5,
                                                                 'max': 5}))

    url = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Entry
        fields = ('happiness', 'disgust', 'url')
