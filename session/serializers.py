from session.models import Session
from rest_framework import serializers


class SessionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Session
        fields = '__all__'
