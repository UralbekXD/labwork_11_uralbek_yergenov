from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=2048, null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, verbose_name='Стоимость')
    image = models.URLField(max_length=1024, null=True, blank=True, verbose_name='Ссылка на изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')

    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='products',
    )

    def __str__(self):
        return f'{self.pk} {self.name} {self.category} {self.price}'
