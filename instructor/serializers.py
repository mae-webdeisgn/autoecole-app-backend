from instructor.models import Instructor
from rest_framework import serializers


class InstructorSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Instructor
        fields = "__all__"