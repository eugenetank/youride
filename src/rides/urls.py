from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rides import views

urlpatterns = [
    path('cars/', views.CarsList.as_view()),
    path('cars/<int:pk>/', views.CarDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
