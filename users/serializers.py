from users.models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'phone', 'street', 'city', 'postalcode', 'country', 'birthday', 'bio', 'email', 'is_student']

class InstructorSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'phone', 'street', 'city', 'postalcode', 'country', 'birthday', 'bio', 'email', 'is_instructor']