from django.shortcuts import render, redirect
from firstapp.models import cultural
from firstapp.forms import CulturalForm
from . import forms
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



# View to display cultural details
def culDetail(request):
    name = 'sakthi'
    cul_data = cultural.objects.all()  # Collecting data from models
    cul_dict = {'cul_list': cul_data}  # Dictionary to pass data
    return render(request, 'firstapp/cultural.html', context=cul_dict)  # Sending data to HTML

# View to handle the cultural form
def form_view(request):
    form = forms.CulturalForm()
    if request.method == 'POST':
        form = forms.CulturalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cultural')  # Redirecting back to cultural view
    return render(request, 'firstapp/home.html', {'form': form})

# View to generate the PDF
def cultural_pdf(request):
    buffer = io.BytesIO()  # Create bytestream buffer
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)  # Create canvas
    textob = c.beginText()  # Create text object
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 24)
    
    lines = [
        "Cultural Festival",
        "Cultural Festival",
        "Cultural Festival",
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='cultural.pdf')


