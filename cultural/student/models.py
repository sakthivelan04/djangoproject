from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    register_no = models.IntegerField(unique=True)
    email = models.EmailField(unique=True, max_length=50)
    collage = models.CharField(max_length=50)
    password = models.CharField(max_length=10)


