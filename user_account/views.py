from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PetsSerializer
from .models import Pets


@api_view(['GET', 'POST'])
def api_pets(request):
    if request.method == 'GET':
        pets = Pets.objects.filter(UserId=request.user)
        serializer = PetsSerializer(pets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_pet_detail(request, pk):
    pet = Pets.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = PetsSerializer(pet)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = PetsSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












