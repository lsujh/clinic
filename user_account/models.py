from django.contrib.auth.models import User
from django.db import models


class Pets(models.Model):
    CHANGE_SEX = [('boy', 'МАЛЬЧИК'), ('girl', 'ДЕВОЧКА'), ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_user',
                               verbose_name='Пользователь')
    PetName = models.CharField('Кличка', max_length=50, db_index=True)
    DateOfBirth = models.DateField(
        'Дата рождения', null=True, blank=True, db_index=True)
    PetSex = models.CharField('Пол', max_length=20,
                              choices=CHANGE_SEX, db_index=True)
    PetTypeId = models.ForeignKey(
        'PetTypes', on_delete=models.PROTECT, related_name='pet_type',
        verbose_name='Тип животного')
    BreedId = models.ForeignKey(
        'Breeds', on_delete=models.PROTECT, related_name='pet_breed',
        verbose_name='Порода')
    Weight = models.FloatField('Вес', blank=True, null=True)
    Image = models.ImageField('', upload_to='user', blank=True)

    class Meta:
        ordering = ('PetName',)
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
        db_table = 'Pets'

    def __str__(self):
        return self.PetName


class PetTypes(models.Model):
    PetTypeName = models.CharField('Тип животного', max_length=50, db_index=True)

    class Meta():
        ordering = ('PetTypeName',)
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животного'
        db_table = 'PetTypes'

    def __str__(self):
        return self.PetTypeName


class Breeds(models.Model):
    BreedName = models.CharField('Порода', max_length=50, db_index=True)
    PetTypeId = models.ForeignKey(PetTypes, on_delete=models.PROTECT,
                                  related_name='breed_type',
                                  verbose_name='Тип животного')

    class Meta():
        ordering = ('BreedName',)
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
        db_table = 'Breeds'

    def __str__(self):
        return self.BreedName
