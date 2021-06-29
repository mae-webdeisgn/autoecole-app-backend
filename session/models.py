from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from users.models import User
from organization.models import Organization

# Create your models here.
class Session(models.Model):
    date = models.DateField(null=False)
    hour = models.TimeField(null=True)
    location = models.CharField(max_length=75, blank=True, null=True)
    instructor_id = models.ForeignKey(User, related_name="instructor_id", on_delete=models.CASCADE)
    student_id = models.ForeignKey(User, related_name="student_id", on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    debrief = models.CharField(max_length=1024, blank=True, null=True)
    created = models.DateField(default=timezone.now)
    private_coment = models.CharField(max_length=1024, blank=True, null=True)
    organization = models.ForeignKey(Organization, related_name="student_id", on_delete=models.CASCADE, null=True)