from django.shortcuts import render

# Create your views here.
from instructor.models import Instructor
from instructor.serializers import InstructorSerializer
from rest_framework import viewsets
from rest_framework import permissions


class InstructorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAuthenticated]
