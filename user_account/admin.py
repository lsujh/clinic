from django.contrib import admin
from .models import Pets, Breeds, PetType


@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Breeds)
class BreedsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
