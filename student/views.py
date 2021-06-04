# Create your views here.
from rest_framework.generics import get_object_or_404
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView


class StudentViewSet(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            snippets = Student.objects.all()
            serializer = StudentSerializer(
                snippets, many=True, context={"request": request}
            )
        else:
            print(pk)
            snippets = get_object_or_404(Student.objects.all(), pk=pk)
            serializer = StudentSerializer(snippets, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        instance = get_object_or_404(Student.objects.all(), pk=pk)
        serializer = StudentSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
