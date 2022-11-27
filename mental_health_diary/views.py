import random
from datetime import date, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import EntryForm, ArticleForm, ActivityEntryForm
from .models import Entry, Article, Activity, ActivityEntry


# Create your views here.

def index(request):
    context = {}
    today = date.today()
    seven_days_before = today - timedelta(days=7)
    if request.user.is_authenticated:
        entries = Entry.objects.filter(creator=request.user, date__gte=seven_days_before).order_by('-date')
        for e in entries:
            if e.date == date.today():
                entries = entries[1:]
                break
        context['today'] = Entry.objects.filter(creator=request.user, date=today).order_by('-date')
        print(context['today'])
        context['entries'] = entries
        activity_entries = ActivityEntry.objects.filter(creator=request.user, date__gte=seven_days_before).order_by('-date')
        context['activities'] = activity_entries
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')


def self_help(request):
    MentalHealthAdvice = Article.objects.filter(category="Mental Health Advice")
    Meditation = Article.objects.filter(category="Meditation")
    Mindfulness = Article.objects.filter(category="Mindfulness")
    Sleep = Article.objects.filter(category="Sleep")
    Stress = Article.objects.filter(category="Stress")

    context = {
        "mental_health_advice": MentalHealthAdvice,
        "meditation": Meditation,
        "mindfulness": Mindfulness,
        "sleep": Sleep,
        "stress": Stress
    }

    return render(request, 'main/self_help.html', context=context)


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

    existing_log = Entry.objects.filter(date=date.today(), creator=request.user)
    if existing_log:
        messages.warning(request, "You've already made an emotion log today! Come back tomorrow, or log some activities!")
        return redirect('daily_entry')
    else:
        form = EntryForm()

        if request.method == 'POST':
            form = EntryForm(request.POST)
            creator = request.user
            url = generate_random_slug()
            today = date.today()
            entry = form.save(commit=False)

            if form.is_valid():
                entry.mood = (entry.power + entry.happiness + entry.peace - (entry.disgust + entry.anger + entry.fear))/6
                entry.creator = creator
                entry.url = url
                entry.date = today
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
        activities = ActivityEntry.objects.filter(creator=entry.creator, date=entry.date)
        context_dict['entry'] = entry
        context_dict['activities'] = activities
    except Entry.DoesNotExist:
        context_dict['entry'] = None

    return render(request, 'main/view_entry.html', context=context_dict)

@login_required
def edit_entry(request, entry_slug):
    # View to edit entries

    editing = Entry.objects.get(url=entry_slug)

    if editing.date != date.today():
        messages.warning(request, "Can't edit entries for previous days!")
        return redirect('index')
    try:
        # Try and get the entry being edited by searching by entry_slug
        form = EntryForm(instance=editing)

        if request.method == 'POST':
            form = EntryForm(request.POST, instance=editing)
            if form.is_valid():
                entry = form.save()
            return redirect('index')

        context_dict = {'form': form, 'instance': editing}
    except Entry.DoesNotExist:
        context_dict = {'form': None, 'instance': None}

    return render(request, 'main/edit_entry.html', context = context_dict)

@login_required
def new_activity_entry(request):
    form = ActivityEntryForm()

    if request.method == 'POST':
        form = ActivityEntryForm(request.POST)
        creator = request.user
        url = generate_random_slug()

        entry = form.save(commit=False)

        if form.is_valid():
            entry.creator = creator
            entry.url = url
            form.save(commit=True)
            return redirect('index')

    context = {
        'title': 'Add New Activity Entry',
        'form': form
    }

    return render(request, "main/new_activity_entry.html", context=context)

@login_required
def view_activity_entry(request, entry_slug):
    context_dict = {}

    context_dict['user'] = request.user

    try:
        entry = ActivityEntry.objects.get(url=entry_slug)
        context_dict['entry'] = entry
    except Entry.DoesNotExist:
        context_dict['entry'] = None

    return render(request, 'main/view_activity_entry.html', context=context_dict)

@login_required
def edit_activity_entry(request, entry_slug):
    # View to edit entries

    try:
        # Try and get the entry being edited by searching by entry_slug
        editing = ActivityEntry.objects.get(url = entry_slug)
        form = ActivityEntryForm(instance=editing)

        if request.method == 'POST':
            form = ActivityEntryForm(request.POST, instance=editing)
            if form.is_valid():
                entry = form.save()
            return HttpResponseRedirect(reverse('index'))

        context_dict = {'form': form, 'instance': editing}
    except Entry.DoesNotExist:
        context_dict = {'form': None, 'instance': None}

    return render(request, 'main/edit_activity_entry.html', context = context_dict)
@login_required
def daily_entry(request):
    return render(request, "main/daily_entry.html")


def generate_random_slug():
    string = ""
    possible_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(10):
        random_value = random.randint(0, len(possible_values) - 1)
        string += possible_values[random_value]
    return string
