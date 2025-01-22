from django import forms


# Register your models here.

class collage(forms.Form):
    Reg_no = forms.IntegerField()
    Password = forms.CharField()
