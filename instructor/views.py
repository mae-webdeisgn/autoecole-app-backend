# Create your views here.
from rest_framework.generics import get_object_or_404
from instructor.models import Instructor
from instructor.serializers import InstructorSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class InstructorViewSet(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            snippets = Instructor.objects.all()
            serializer = InstructorSerializer(snippets, many=True, context={'request': request})
        else:
            print(pk)
            snippets = get_object_or_404(Instructor.objects.all(), pk=pk)
            serializer = InstructorSerializer(snippets, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        instance = get_object_or_404(Instructor.objects.all(), pk=pk)
        serializer = InstructorSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
