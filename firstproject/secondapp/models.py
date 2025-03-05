from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, help_text='Enter your name')
    register_no = models.IntegerField(unique=True, help_text='Enter your register number')
    email = models.EmailField(max_length=50, help_text='Enter a valid email address')
    collage = models.CharField(max_length=50, help_text='Enter your collage name')
    password = models.CharField(max_length=10)
