from rides.models import Car
from rides.serializers import CarSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User


class CarList(generics.ListCreateAPIView):
    """
    List all or create a new car
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

