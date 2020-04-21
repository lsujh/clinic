from django.urls import path
from .views import all_pets_user, add_pet, edit_pet, delete_pet

app_name = 'user_account'

urlpatterns = [
    path('edit_pet/<int:id>/', edit_pet, name='edit_pet'),
    path('delete_pet/<int:id>/', delete_pet, name='delete_pet'),
    path('add_pet/', add_pet, name='add_pet'),
    path('all_pets_user/', all_pets_user, name='all_pets_user'),
]
