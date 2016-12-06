from __future__ import unicode_literals
from django.db import models

class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to='/home/alisha/mydjango/HelloWorld/ImageGallery/static/')

class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=15)

class Login(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
