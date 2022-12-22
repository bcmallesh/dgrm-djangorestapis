from rest_framework import serializers

from appointments.models import RegisterAppointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterAppointment
        fields = ["patients", "disease", "date", "timings", "description"]
