from django.urls import path
from .views import api_pets, api_pet_detail

app_name = 'api'

urlpatterns = [
    path('pet/<int:pk>/', api_pet_detail),
    path('pets/', api_pets),
]
