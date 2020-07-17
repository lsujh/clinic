from rest_framework import viewsets
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly
from .serializers import PetsSerializer
from .models import Pets

permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer








