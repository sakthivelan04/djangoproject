from django.shortcuts import render,redirect
from .forms import UserForm
from firstapp.forms import collage
from . import models
from firstapp.views import clg

# Create your views here.

def h(request):
    return render(request, 'secondapp/home.html')

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/first/login')
        return render(request,'firstapp/ab.html', {'form': form})
    
           
    else:
        form = UserForm()

    return render(request,'secondapp/register.html', {'form': form})


