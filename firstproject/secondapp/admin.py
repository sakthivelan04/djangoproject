from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'register_no', 'email', 'collage')

admin.site.register(Student, StudentAdmin)
