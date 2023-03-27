from django.db import models

# Create your models here.
class Sample(models.Model):
    recipe_name = models.CharField(max_length=10)
    recipe_image = models.ImageField(upload_to='Sample')
    ingredients = models.TextField(max_length=200)
    instructions = models.TextField(max_length=200)

class Simple(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=200)