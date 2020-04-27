from django.contrib import admin
from .models import Pets, Breeds, PetTypes


class PetsAdmin(admin.ModelAdmin):
    model = Pets
    list_display = ('PetId', 'PetName', 'UserId')

admin.site.register(Pets, PetsAdmin)
admin.site.register(PetTypes)
admin.site.register(Breeds)
