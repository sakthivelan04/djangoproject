from django.db import models

# Create your models here.

class cultural(models.Model):
    Clg_Name = models.CharField(max_length=50)
    Clg_Address = models.CharField(max_length=100)
    Event_Name = models.CharField(max_length=200)
    Date = models.DateField(null=True, blank=True)
    cultural_Poster = models.ImageField(null=True, blank=True, upload_to="images/")
    

