from django.db import models

# Create your models here.
class Registerdb(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    fullname = models.CharField(max_length=20)
    email = models.CharField(max_length=15)
    phone = models.TextField(max_length=12)