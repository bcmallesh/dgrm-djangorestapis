from rest_framework import generics, status
from rest_framework.response import Response

from appointments.models import RegisterAppointment
from appointments.serializers import AppointmentSerializer


# Create your views here.
class AppointmentView(generics.ListCreateAPIView):

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleAppointmentView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request, pk):
        appointment = RegisterAppointment.objects.get(id=pk)
        serializer = AppointmentSerializer(appointment)
        if appointment:
            # appointments = RegisterAppointment.objects.filter(patients=patient)
            # if appointments:
            #     appointmentserializer = AppointmentSerializer(appointments, many=True)
            #     bookappointments = appointmentserializer.data
            #
            # serializer.data.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        appointment = RegisterAppointment.objects.get(id=pk)
        serializer = AppointmentSerializer(appointment, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appointment = RegisterAppointment.objects.get(id=pk)
        serializer = AppointmentSerializer(appointment)
        if appointment:
            appointment.delete()
            return Response({"status": "ok"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MultipleAppointmentView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request):
        appointments = RegisterAppointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
