from django import forms
from .models import cultural
from events.models import register


# Register your models here.


class CulturalForm(forms.ModelForm):
    class Meta:
        model = cultural
        fields = '__all__'
        #exclude = ['password']
        
        
class regigterform(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'        
        