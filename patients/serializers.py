from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from appointments.models import RegisterAppointment
from patients.models import RegisterUser


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        appointments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

        model = RegisterUser

        fields = ["user_name", "user_email", "password", "user_dob", "location", "user_mobile", 'appointments']
