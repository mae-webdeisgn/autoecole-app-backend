from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from users.models import User
from users.serializers import StudentSerializer
from users.serializers import InstructorSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView

# Create your views here.
class StudentAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = User.objects.filter(is_student=True)
            serializer = StudentSerializer(
                instance, many=True, context={"request": request}
            )
        else:
            instance = get_object_or_404(User.objects.filter(pk=pk, is_student=True))
            serializer = StudentSerializer(instance, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        instance = get_object_or_404(User.objects.filter(pk=pk))
        serializer = StudentSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(User.objects.filter(pk=pk))
        serializer = StudentSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstructorAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            snippets = User.objects.filter(is_instructor=True)
            serializer = InstructorSerializer(
                snippets, many=True, context={"request": request}
            )
        else:
            snippets = get_object_or_404(User.objects.filter(pk=pk, is_instructor=True))
            serializer = InstructorSerializer(snippets, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = get_object_or_404(User.objects.all(), pk=pk)
        serializer = InstructorSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(User.objects.all(), pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)