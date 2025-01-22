from django.contrib import admin
from firstapp.models import cultural

# Register your models here.

class CulturalAdmin(admin.ModelAdmin):
    list_display = ('Clg_Name','Clg_Address','Event_Name')
admin.site.register(cultural,CulturalAdmin)
