from rest_framework import serializers

from .models import Car
from django.contrib.auth.models import User


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(required=False, max_length=30, allow_blank=True)
    model = serializers.CharField(required=True, max_length=30)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        """
        Create and return a new `Car` instance, given the validated data.
        :param validated_data:
        :return:
        """
        return Car.objects.create(**validated_data)
    class Meta:
        model = Car
        fields = ('manufacturer', 'model', 'production_year', 'seats', 'id', 'owner',)

