from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models


class Pets(models.Model):
    CHANGE_SEX = [('boy', 'МАЛЬЧИК'), ('girl', 'ДЕВОЧКА'), ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_user', verbose_name='Пользователь')
    name = models.CharField('Кличка', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    date_of_birth = models.DateField(
        'Дата рождения', null=True, blank=True, db_index=True)
    sex = models.CharField('Пол', max_length=20,
                           choices=CHANGE_SEX, db_index=True)
    type = models.ForeignKey(
        'PetType', on_delete=models.PROTECT, related_name='pet_type',
        verbose_name='Тип животного')
    breed = models.ForeignKey(
        'Breeds', on_delete=models.PROTECT, related_name='pet_breed',
        verbose_name='Порода')
    weight = models.FloatField('Вес', blank=True, null=True)
    image = models.ImageField('', upload_to='pets/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_account:all_pets_user', args=[self.slug])


class PetType(models.Model):
    name = models.CharField('Тип животного', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    class Meta():
        ordering = ('name',)
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животного'

    def __str__(self):
        return self.name


class Breeds(models.Model):
    name = models.CharField('Порода', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    type = models.ForeignKey(PetType, on_delete=models.PROTECT,
                             related_name='breed_type',
                             verbose_name='Тип животного')

    class Meta():
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.name
