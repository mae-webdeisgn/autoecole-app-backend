from users.models import User
from rest_framework import serializers

class UserGenericSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get("firstname", instance.firstname)
        instance.lastname = validated_data.get("lastname", instance.lastname)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.street = validated_data.get("street", instance.street)
        instance.city = validated_data.get("city", instance.city)
        instance.postalcode = validated_data.get("postalcode", instance.postalcode)
        instance.country = validated_data.get("country", instance.country)
        instance.birthday = validated_data.get("birthday", instance.birthday)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "firstname",
            "lastname",
            "phone",
            "street",
            "city",
            "postalcode",
            "country",
            "birthday",
            "bio",
            "email",
        ]
    pass

class StudentSerializer(UserGenericSerializer):
    def create(self, validated_data):
        validated_data["is_student"] = True
        return User.objects.create(**validated_data)


class InstructorSerializer(UserGenericSerializer):
    def create(self, validated_data):
        validated_data["is_instructor"] = True
        return User.objects.create(**validated_data)
