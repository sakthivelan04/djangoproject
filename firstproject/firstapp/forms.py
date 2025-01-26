from django import forms
from .models import cultural


# Register your models here.

class collage(forms.Form):
    Reg_no = forms.IntegerField()
    Password = forms.CharField()

class CulturalForm(forms.ModelForm):
    class Meta:
        model = cultural
        fields = '__all__'
        #exclude = ['password']
        