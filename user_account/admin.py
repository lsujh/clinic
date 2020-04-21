from django.contrib import admin
from .models import Pets, Breeds, PetTypes

admin.site.register(Pets)
admin.site.register(PetTypes)
admin.site.register(Breeds)
