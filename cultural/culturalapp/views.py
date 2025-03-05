from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from events.models import cultural

def culDetail(request):
    name = 'sakthi'
    cul_data = cultural.objects.all() # Collecting data from models
    cul_dict = {'cul_list': cul_data}  # Dictionary to pass data
    return render(request,'culturalapp/events.html', context=cul_dict) 


# Create your views here.
@login_required
def home(request):
    return render(request, "culturalapp/index.html", {} )

def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None) 
        if form.is_valid():
            form.save()
        return redirect('login')    
    else:
     form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form": form})

