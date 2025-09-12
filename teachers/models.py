from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Teacher(models.Model):
    full_name_ru = models.CharField(max_length=255, verbose_name='ФИО (русский)')
    full_name_kg = models.CharField(max_length=255, verbose_name='ФИО (кыргызский)')
    full_name_en = models.CharField(max_length=255, verbose_name='ФИО (английский)')

    position_ru = models.CharField(max_length=255, verbose_name='Должность (русский)')
    position_kg = models.CharField(max_length=255, verbose_name='Должность (кыргызский)')
    position_en = models.CharField(max_length=255, verbose_name='Должность (английский)')

    bio_ru = models.TextField(verbose_name='Биография (русский)')
    bio_kg = models.TextField(verbose_name='Биография (кыргызский)')
    bio_en = models.TextField(verbose_name='Биография (английский)')

    photo = models.ImageField(upload_to='teachers/photos/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.full_name_ru

class Management(MPTTModel):
    full_name_ru = models.CharField(max_length=255, verbose_name='ФИО (русский)')
    full_name_kg = models.CharField(max_length=255, verbose_name='ФИО (кыргызский)', blank=True)
    full_name_en = models.CharField(max_length=255, verbose_name='ФИО (английский)', blank=True)

    position_ru = models.CharField(max_length=255, verbose_name='Должность (русский)')
    position_kg = models.CharField(max_length=255, verbose_name='Должность (кыргызский)', blank=True)
    position_en = models.CharField(max_length=255, verbose_name='Должность (английский)', blank=True)

    bio_ru = models.TextField(verbose_name='Биография (русский)', blank=True)
    bio_kg = models.TextField(verbose_name='Биография (кыргызский)', blank=True)
    bio_en = models.TextField(verbose_name='Биография (английский)', blank=True)

    photo = models.ImageField(upload_to='management/photos/', verbose_name='Фото', blank=True, null=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Вышестоящий')

    class MPTTMeta:
        order_insertion_by = ['full_name_ru']

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководство'

    def __str__(self):
        return self.full_name_ru
