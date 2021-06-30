from session.models import Session
from users.serializers import InstructorSerializer, StudentSerializer
from rest_framework import serializers


class SessionSerializerGet(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    student_id = StudentSerializer()
    instructor_id = InstructorSerializer()
    class Meta:
        model = Session
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Session
        fields = '__all__'