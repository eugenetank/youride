from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Other'),
    ]

    address = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    phone_number = models.CharField(max_length=32, default='')
    is_blocked = models.BooleanField(default=False)
