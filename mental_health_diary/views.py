import random

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

from .forms import EntryForm, ArticleForm
from .models import Entry, Article


# Create your views here.

def index(request):
    context = {}
    if request.user.is_authenticated:
        entries = Entry.objects.filter(creator=request.user)
        context['entries'] = entries
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')


def self_help(request):
    MentalHealthAdvice = Article.objects.filter(category="1")
    Meditation = Article.objects.filter(category="2")
    Mindfulness = Article.objects.filter(category="3")
    Sleep = Article.objects.filter(category="4")
    Stress = Article.objects.filter(category="5")

    context = {
        "mental_health_advice": MentalHealthAdvice,
        "meditation": Meditation,
        "mindfulness": Mindfulness,
        "sleep": Sleep,
        "stress": Stress
    }

    return render(request, 'main/self_help.html', context=context)


def settings(request):
    return render(request, 'main/settings.html')


def disclaimer(request):
    return render(request, 'main/disclaimer.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def new_entry(request):
    form = EntryForm()

    if request.method == 'POST':
        form = EntryForm(request.POST)
        creator = request.user
        url = generate_random_slug()

        entry = form.save(commit=False)

        if form.is_valid():
            entry.creator = creator
            entry.url = url
            form.save(commit=True)
            return redirect('index')

    context = {
        'title': 'Add New Entry',
        'form': form
    }

    return render(request, "main/new_entry.html", context=context)


def new_article(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, "main/new_article.html", context=context)


@login_required
def view_entry(request, entry_slug):
    context_dict = {}

    context_dict['user'] = request.user

    try:
        entry = Entry.objects.get(url=entry_slug)
        context_dict['entry'] = entry
    except Entry.DoesNotExist:
        context_dict['entry'] = None

    return render(request, 'main/view_entry.html', context=context_dict)

@login_required
def edit_entry(request, entry_slug):
    # View to edit entries

    try:
        # Try and get the entry being edited by searching by entry_slug
        editing = Entry.objects.get(url = entry_slug)
        form = EntryForm(instance=editing)

        if request.method == 'POST':
            form = EntryForm(instance=editing)
            if form.is_valid():
                entry = form.save()
            return HttpResponseRedirect(reverse('main:index'))

        context_dict = {'form': form, 'instance': editing}
    except Entry.DoesNotExist:
        context_dict = {'form': None, 'instance': None}

    return render(request, 'main/edit_entry.html', context = context_dict)




def generate_random_slug():
    string = ""
    possible_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(10):
        random_value = random.randint(0, len(possible_values) - 1)
        string += possible_values[random_value]
    return string
