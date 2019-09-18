from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class Car(models.Model):
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    production_year = models.DecimalField(max_digits=4, decimal_places=0, validators=[
        MinValueValidator(1938),
        MaxValueValidator(2019)
    ])
    seats = models.IntegerField(default=4, validators=[
        MinValueValidator(1),
        MaxValueValidator(50)
    ])
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Ride(models.Model):
    distance = models.IntegerField()
    duration = models.IntegerField()
    departure_datetime = models.DateTimeField()
    departure_delta = models.DurationField()
    created_at = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
