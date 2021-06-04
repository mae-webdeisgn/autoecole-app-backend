from django.db import models
from django.db.models.deletion import CASCADE
from student.models import Student
from instructor.models import Instructor
from django.utils import timezone


# Create your models here.
class Session(models.Model):
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    location = models.CharField(max_length=75, blank=True, null=True)
    instructor_id = models.ForeignKey(Instructor, on_delete=CASCADE)
    student_id = models.ForeignKey(Student, on_delete=CASCADE)
    active = models.BooleanField(default=True)
    debrief = models.CharField(max_length=1024, blank=True, null=True)
    created = models.DateField(default=timezone.now)
    private_coment = models.CharField(max_length=1024, blank=True, null=True)
