from rest_framework import serializers
from .models import Pets


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ['user_id', 'pet_name', 'date_of_birth', 'pet_sex',
                  'pet_type_id', 'breed_id', 'weight', 'image']




