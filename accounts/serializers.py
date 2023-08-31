from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    


