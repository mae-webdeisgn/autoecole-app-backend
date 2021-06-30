from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=14, null=True)
    address = models.CharField(max_length=150, null=True)
    email = models.EmailField()
