from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form' : form,
    }
    return render(request, 'authen/signup.html', context )


def index(request):
    return render(request, 'main/index.html', {})

def home(request):
    return render(request, 'main/home.html', {})
