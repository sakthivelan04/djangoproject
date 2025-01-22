from django.contrib import admin
from secondapp.models import Student

# Register your models here.

class StudentModelsAdmin(admin.ModelAdmin):
    list_display = ('username','register_no','password')
admin.site.register(Student,StudentModelsAdmin)
    
