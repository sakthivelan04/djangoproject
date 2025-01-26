from django.shortcuts import render
#from django.http import HttpResponce
from firstapp.models import cultural
from firstapp.forms import CulturalForm
from . import forms
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def  culDetail(request):
    name = 'sakthi'
    cul_data = cultural.objects.all()  #collecting data from models
    cul_dict = {'cul_list': cul_data}#dictionary
    return render(request, 'firstapp/a1.html', context = cul_dict )  # send the data to html

def form_view(request):
    form = forms.CulturalForm()
    if request.method == 'POST':
        form = forms.CulturalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return culDetail(request)
    return render(request, 'firstapp/update.html', {'form': form})

def clg(request):
    form = forms.collage()
    clg_info = {'form' :form}
    return render(request,'firstapp/ab.html', context = clg_info)

def cultural_pdf(request):
    buffer = io.BytesIO()   # create bytestream buffer
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)  #create a canvas
    textob = c.beginText()     # create a text object
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 24)
    line =[
        "Cultural Festival",
        "Cultural Festival",
        "Cultural Festival",
    ]
    for i in line:
        textob.textLine(i)
        c.drawText(textob)
        c.showPage()
        c.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='cultural.pdf')