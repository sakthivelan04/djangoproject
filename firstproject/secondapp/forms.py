from django import forms
from .models import Student

class UserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)
     confirm_password = forms.CharField(widget=forms.PasswordInput)

     class Meta:
        model = Student
        fields = ('username','register_no','collage','password')

     def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password do not match"
            )



