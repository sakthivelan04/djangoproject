from django.db import models



# Create your models here.

class cultural(models.Model):
    id = models.AutoField(primary_key=True)
    Clg_Name = models.CharField(max_length=50)
    Clg_Address = models.CharField(max_length=100)
    Event_Name = models.CharField(max_length=200)
    Date = models.DateField(null=True, blank=True)
    cultural_Poster = models.ImageField(null=True, blank=True, upload_to="images/")
    
class register(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)
    Number = models.CharField(max_length=10)
    College_name = models.CharField(max_length=50)
    Event_name = models.CharField(max_length=20)
    
    