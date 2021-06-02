from session.models import Session
from rest_framework import serializers


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['date', 'instructor_id', 'student_id', 'active']