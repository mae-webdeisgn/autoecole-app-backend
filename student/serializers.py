from student.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Student
        fields = "__all__"
