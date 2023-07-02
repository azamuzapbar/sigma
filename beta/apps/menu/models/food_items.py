from django.core.validators import MinValueValidator
from django.db import models
from .menu import Menu

class FoodItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    price = models.IntegerField(validators=[MinValueValidator(0)], default=0, verbose_name='Цена')

    def __str__(self):
        return self.name
