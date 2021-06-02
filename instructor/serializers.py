from instructor.models import Instructor
from rest_framework import serializers


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'phone_number']