from django.db import models

# Create your models here.
class Login(models.Model):    
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Register(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)