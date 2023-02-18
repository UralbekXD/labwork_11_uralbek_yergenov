from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=2048, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.pk} {self.name}'
