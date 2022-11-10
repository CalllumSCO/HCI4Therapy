import random

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import EntryForm


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def self_help(request):
    return render(request, 'main/self_help.html')


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


#def new_entry(request):
    #View used to create a new entry

    #form = EntryForm()

    #if request.method == 'POST':
        #form = EntryForm(request.POST)
        #user = request.user
        #url = generate_random_slug()

        #entry = form.save(commit=False)

        #if form.is_valid():
            #entry.user = user
            #entry.url = url
            #form.save(commit=True)

        #context = {
            #'title' : 'Add New Entry',
            #'form' : form
        #}

        #return render(request, "main/index.html", context=context)

def generate_random_slug():
    string = ""
    possible_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(10):
        random_value = random.randint(0, len(possible_values)-1)
        string += possible_values[random_value]
    return string
