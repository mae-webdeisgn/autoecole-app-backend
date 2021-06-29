from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=14, default="")
    address = models.CharField(max_length=150, default="")
    email = models.EmailField()
