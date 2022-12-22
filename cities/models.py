from django.db import models
from django.urls import reverse


class City(models.Model):
    """Модель города"""
    name = models.CharField(max_length=255, verbose_name='Город')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cities:home')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

