from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
# Create your views here.
from django.urls import reverse

from accounts.forms import EmployeeUserCreationForm


def register_view(request):
    form = EmployeeUserCreationForm()
    if request.method == 'POST':
        form = EmployeeUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Successfully Registered')
            return redirect(reverse('register'))
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return render(request, 'login.html',
                          {'form': AuthenticationForm(), 'error': 'The Username & Password Are Wrong..!'})
        else:
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def logout(request):
    auth.logout(request)
    return redirect('login')
