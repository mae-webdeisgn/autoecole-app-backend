from django.db import models

# Create your models here.
class Instructor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=14)
    email = models.EmailField(default="contact@izidi.com")