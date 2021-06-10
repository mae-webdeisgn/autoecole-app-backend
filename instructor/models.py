from django.db import models

# Create your models here.
class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()