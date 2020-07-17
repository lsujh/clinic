from django.contrib.auth.models import User
from django.db import models


class ClinicPetTypes(models.Model):
    clinic_pet_type_id = models.IntegerField(
        db_column='ClinicPetTypeId', primary_key=True)
    clinic_id = models.ForeignKey(
        'Clinics', models.DO_NOTHING, db_column='ClinicId')
    pet_type_id = models.ForeignKey(
        'PetTypes', models.DO_NOTHING, db_column='PetTypeId')

    class Meta:
        db_table = 'ClinicPetTypes'

class Clinics(models.Model):
    clinic_id = models.IntegerField(db_column='ClinicId', primary_key=True)
    clinic_name = models.CharField(db_column='ClinicName', max_length=50)
    phone_number = models.CharField(db_column='PhoneNumber', max_length=25)
    city = models.CharField(db_column='City', max_length=50)
    street = models.CharField(db_column='Street', max_length=50)
    house = models.CharField(db_column='House', max_length=10)
    housing = models.CharField(
        db_column='Housing', max_length=10, blank=True, null=True)
    short_info = models.TextField(db_column='ShortInfo', blank=True, null=True)
    psrn = models.IntegerField(db_column='PSRN')
    tin = models.IntegerField(db_column='TIN')
    rrs = models.IntegerField(db_column='RRS')

    class Meta:
        db_table = 'Clinics'

class PetTypes(models.Model):
    pet_type_id = models.IntegerField(db_column='PetTypeId', primary_key=True)
    pet_type_name = models.CharField(db_column='PetTypeName', max_length=50)

    class Meta:
        ordering = ('pet_type_name',)
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животного'
        db_table = 'PetTypes'

    def __str__(self):
        return self.pet_type_name

class Breeds(models.Model):
    breed_id = models.IntegerField(db_column='BreedId', primary_key=True)
    breed_name = models.CharField(db_column='BreedName', max_length=50)
    pet_type_id = models.ForeignKey(
        PetTypes, models.DO_NOTHING, db_column='PetTypeId')

    class Meta:
        ordering = ('breed_name',)
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
        db_table = 'Breeds'

    def __str__(self):
        return self.breed_name


class Pets(models.Model):
    CHANGE_SEX = [('boy', 'МАЛЬЧИК'), ('girl', 'ДЕВОЧКА'), ]
    pet_id = models.IntegerField(db_column='PetId', primary_key=True)
    user_id = models.CharField(db_column='UserId', max_length=36)
    pet_name = models.CharField('Кличка', db_column='PetName', max_length=50)
    date_of_birth = models.DateTimeField('Дата рождения',
        db_column='DateOfBirth', blank=True, null=True)
    pet_sex = models.CharField('Пол', db_column='PetSex', max_length=10, choices=CHANGE_SEX)
    pet_type_id = models.ForeignKey(
        PetTypes, models.DO_NOTHING, db_column='PetTypeId', verbose_name='Тип животного')
    breed_id = models.ForeignKey(
        Breeds, models.DO_NOTHING, db_column='BreedId', verbose_name='Порода')
    weight = models.FloatField('Вес', db_column='Weight', blank=True, null=True)
    image = models.ImageField('Фотоup', db_column='Image', upload_to='media/', blank=True)

    class Meta:
        db_table = 'Pets'
        ordering = ('pet_name',)
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self):
        return self.pet_name
