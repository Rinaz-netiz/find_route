from django.db import models


class City(models.Model):
    """Модель города"""
    name = models.CharField(max_length=255, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

