from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Entry, Article, ActivityEntry, Activity
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EntryForm(forms.ModelForm):
    happiness = forms.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(5)],
                                   help_text="Please rate your happiness for today from -5 to 5.",
                                   widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                   'placeholder': '-5 - 5',
                                                                   'min': -5,
                                                                   'max': 5}))
    anger = forms.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(5)],
                               help_text="Please rate your anger for today from -5 to 5.",
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': '-5 - 5',
                                                               'min': -5,
                                                               'max': 5}))

    disgust = forms.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(5)],
                                 help_text="Please rate your disgust today from -5 to 5.",
                                 widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                 'placeholder': '-5 - 5',
                                                                 'min': -5,
                                                                 'max': 5}))

    fear = forms.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(5)],
                              help_text="Please rate your fear today from -5 to 5.",
                              widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'placeholder': '-5 - 5',
                                                              'min': -5,
                                                              'max': 5}))

    power = forms.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(5)],
                               help_text="Please rate your feeling of power today from -5 to 5.",
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': '-5 - 5',
                                                               'min': -5,
                                                               'max': 5}))
    peace = forms.IntegerField(validators=[MinValueValidator(-5), MaxValueValidator(5)],
                               help_text="Please rate your feeling of peace today from -5 to 5.",
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': '-5 - 5',
                                                               'min': -5,
                                                               'max': 5}))

    url = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Entry
        fields = ('happiness', 'anger', 'disgust', 'fear', 'power', 'peace', 'url')


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
    url = forms.URLField(max_length=200)

    class Meta:
        model = Article
        fields = ('title', 'category', 'url')


def generate_activity_choices():
    choices = ()
    activities = list(Activity.objects.values('activity'))
    i = 1
    for a in activities:
        val = list(a.values())
        print(val)
        choice = (str(i), Activity.objects.get(activity=val[0]))
        choices = choices + (choice,)
        i += 1
    print(choices)

    return choices


class ActivityEntryForm(forms.ModelForm):
    activity = forms.ModelChoiceField(queryset=Activity.objects.all().order_by('activity'), label='Select Activity',
                                 widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Activity'}),
                                 help_text="Choose an Activity")

    time = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1720)],
                              help_text="Please enter the duration of this task.")

    class Meta:
        model = ActivityEntry
        fields = ('activity', 'time')
