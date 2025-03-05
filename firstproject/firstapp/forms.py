from django import forms
from .models import cultural


# Register your models here.


class CulturalForm(forms.ModelForm):
    class Meta:
        model = cultural
        fields = '__all__'
        #exclude = ['password']
        