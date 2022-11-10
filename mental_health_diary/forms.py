from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Entry, Article
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


article_category_choices = (
    ("1", "Mental Health Advice"),
    ("2", "Meditation"),
    ("3", "Mindfulness"),
    ("4", "Sleep"),
    ("5", "Stress"),
)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=256, help_text="Please enter the title for your article",
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    category = forms.ChoiceField(choices=article_category_choices)
    description = forms.CharField(max_length=512, help_text="Enter a description of the article",
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control', 'placeholder': 'A description of the article'}))
    url = forms.URLField(max_length=200)

    class Meta:
        model = Article
        fields = ('title', 'category', 'description', 'url')
