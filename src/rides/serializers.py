from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Car

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('manufacturer', 'model', 'production_year', 'seats', 'id', 'owner',)


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

