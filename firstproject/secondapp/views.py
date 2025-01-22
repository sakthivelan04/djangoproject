from django.shortcuts import render,redirect
from .forms import UserForm
from . import models

# Create your views here.

def h(request):
    return render(request, 'secondapp/home.html')

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'secondapp/home.html', {'form': form})
           
    else:
        form = UserForm()

    return render(request,'secondapp/register.html', {'form': form})


