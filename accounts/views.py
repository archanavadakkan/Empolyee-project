from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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
    return render(request,'login.html')
