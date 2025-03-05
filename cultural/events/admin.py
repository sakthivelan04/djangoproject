from django.contrib import admin
from events.models import cultural
from events.models import register

# Register your models here.

class CulturalAdmin(admin.ModelAdmin):
    list_display = ('Clg_Name','Clg_Address','Event_Name','Date','cultural_Poster')
admin.site.register(cultural,CulturalAdmin)


class registerAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Email','Number','College_name','Event_name')
admin.site.register(register,registerAdmin)