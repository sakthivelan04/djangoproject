from django.shortcuts import render
#from django.http import HttpResponce
from firstapp.models import cultural
from . import forms

# Create your views here.

def  culDetail(request):
    name = 'sakthi'
    cul_data = cultural.objects.all()  #collecting data from models
    cul_dict = {'cul_list': cul_data}  #dictionary
    return render(request, 'firstapp/a1.html', context = cul_dict )  # send the data to html


def clg(request):
    form = forms.collage()
    clg_info = {'form' :form}
    return render(request,'firstapp/ab.html', context = clg_info)
