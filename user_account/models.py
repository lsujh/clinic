from django.contrib.auth.models import User
from django.db import models


class Pets(models.Model):
    CHANGE_SEX = [('boy', 'МАЛЬЧИК'), ('girl', 'ДЕВОЧКА'), ]
    pet_id = models.AutoField(primary_key=True, db_column='PetId')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_user',
                                verbose_name='Пользователь', db_column='UserId')
    pet_name = models.CharField('Кличка', max_length=50, db_index=True, db_column='PetName')
    date_of_birth = models.DateField(
        'Дата рождения', null=True, blank=True, db_index=True, db_column='DateOfBirth')
    pet_sex = models.CharField('Пол', max_length=20,
                               choices=CHANGE_SEX, db_index=True, db_column='PetSex')
    pet_type_id = models.ForeignKey(
        'PetTypes', on_delete=models.PROTECT, related_name='pet_type',
        verbose_name='Тип животного', db_column='PetTypeId')
    breed_id = models.ForeignKey(
        'Breeds', on_delete=models.PROTECT, related_name='pet_breed',
        verbose_name='Порода', db_column='BreedId')
    weight = models.FloatField('Вес', blank=True, null=True, db_column='Weight')
    image = models.ImageField('', upload_to='user_id', blank=True, db_column='Image')

    class Meta:
        ordering = ('pet_name',)
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
        db_table = 'Pets'

    def __str__(self):
        return self.pet_name


class PetTypes(models.Model):
    pet_type_id = models.AutoField(primary_key=True, db_column='PetTypeId')
    pet_type_name = models.CharField('Тип животного', max_length=50, db_index=True, db_column='PetTypeName')

    class Meta:
        ordering = ('pet_type_name',)
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животного'
        db_table = 'PetTypes'

    def __str__(self):
        return self.pet_type_name


class Breeds(models.Model):
    breed_id = models.AutoField(primary_key=True, db_column='BreedId')
    breed_name = models.CharField('Порода', max_length=50, db_index=True, db_column='BreedName')
    pet_type_id = models.ForeignKey(PetTypes, on_delete=models.PROTECT,
                                    related_name='breed_type',
                                    verbose_name='Тип животного', db_column='PetTypeId')

    class Meta:
        ordering = ('breed_name',)
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
        db_table = 'Breeds'

    def __str__(self):
        return self.breed_name
