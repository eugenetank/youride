from django.db import models


class Car(models.Model):
    brand_name = models.CharField(max_length=100)
    production_year = models.IntegerField()


