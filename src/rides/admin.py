from django.contrib import admin
from rides.models import Car


class CarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Car, CarAdmin)
# Register your models here.
