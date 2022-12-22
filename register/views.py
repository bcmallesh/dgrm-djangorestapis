from django.contrib import auth
from rest_framework import generics, status
from rest_framework.response import Response

from register.models import RegisterUser
from register.serializers import RegisterUserSerializer, SigninUserSerializer


# Create your views here.
class RegisterView(generics.ListCreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignView(generics.GenericAPIView):
    def get(self, request):
        user_email = request.data["user_email"]
        password = request.data["password"]
        user = RegisterUser.objects.get(user_email=user_email, password=password)
        if user is not None:
            serializer = RegisterUserSerializer(user)
            return Response(serializer.data)


class SingleUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SigninUserSerializer

    def get(self, request, pk):
        user = RegisterUser.objects.get(id=pk)
        serializer = RegisterUserSerializer(user)
        return Response(serializer.data)

    def post(self, request, pk):
        user = RegisterUser.objects.get(id=pk)
        serializer = RegisterUserSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
