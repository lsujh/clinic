from rest_framework import serializers
from .models import Pets


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ('UserId', 'PetName', 'DateOfBirth', 'PetSex', 'PetTypeId', 'BreedId', 'Weight', 'Image')




