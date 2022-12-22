from rest_framework import generics, status
from rest_framework.response import Response

from appointments.models import RegisterAppointment
from appointments.serializers import AppointmentSerializer
from patients.models import RegisterUser
from patients.serializers import RegisterUserSerializer


# Create your views here.
class PatientView(generics.ListCreateAPIView):

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleUserView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request, pk):
        patient = RegisterUser.objects.get(id=pk)
        serializer = RegisterUserSerializer(patient)
        if patient:
            # appointments = RegisterAppointment.objects.filter(patients=patient)
            # if appointments:
            #     appointmentserializer = AppointmentSerializer(appointments, many=True)
            #     bookappointments = appointmentserializer.data
            #
            # serializer.data.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        patient = RegisterUser.objects.get(id=pk)
        serializer = RegisterUserSerializer(patient, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = RegisterUser.objects.get(id=pk)
        user.delete(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MultipleUserView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request):
        users = RegisterUser.objects.all()
        serializer = RegisterUserSerializer(users, many=True)
        return Response(serializer.data)
