from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from session.models import Session
from session.serializers import SessionSerializer, SessionSerializerGet
from django.http import Http404


class Sessions(APIView):
    def get(self, request, pk=None):
        if pk is None:
            instances = Session.objects.all()
            serializer = SessionSerializerGet(
                instances, many=True, context={"request": request}
            )
        else:
            instances = get_object_or_404(Session.objects.filter(pk=pk))
            serializer = SessionSerializerGet(instances, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        instance = get_object_or_404(Session.objects.all(), pk=pk)
        serializer = SessionSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
