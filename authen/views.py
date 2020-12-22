from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import (
    LoginView,
    LogoutView as Logout
)    
# Create your views here.

class Login(LoginView):
    template_name = 'authen/login.html'
    redirect_authenticated_user = True

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
