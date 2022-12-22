from rest_framework import serializers

from register.models import RegisterUser


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ["user_name", "user_email", "password", "user_dob", "location", "user_mobile"]


class SigninUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ["user_email", "password"]

