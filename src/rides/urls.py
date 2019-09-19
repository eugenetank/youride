from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rides import views

urlpatterns = [
    path('cars/', views.cars_list),
    path('cars/<int:pk>/', views.car_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
