from django.db import models

# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=20)
    register_no = models.CharField(max_length=20)
    collage = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

  
    

   
