from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(
        max_length=50,
    )
    phone = models.CharField(
        max_length=14,
    )
    street = models.CharField(
        max_length=75,
    )
    city = models.CharField(max_length=75)
    postalcode = models.CharField(max_length=7)
    country = models.CharField(
        max_length=30,
    )
    email = models.EmailField()
