from django.shortcuts import render
from session.models import Session
from session.serializers import SessionSerializerGet
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, time

# Create your views here.
class Schedules(APIView):
    def get(self, request, pk, day):
        queryset = Session.objects.filter(instructor_id=pk, day=day)
        session_serializer = SessionSerializerGet(queryset, many=True)
        list_working_hour = [time(i) for i in range(6, 18)]
        list_hour_scheduled = [datetime.strptime(i['hour'], '%H:%M:%S').time() for i in session_serializer.data]
        list_available_hour = [hour for hour in list_working_hour if hour not in list_hour_scheduled]
        result = dict(hour=list_available_hour, instructor_id=pk, day=day)
        return Response(result)
