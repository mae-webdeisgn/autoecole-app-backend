from django.shortcuts import render

# Create your views here.
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import permissions


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
