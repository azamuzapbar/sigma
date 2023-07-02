from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    description = models.TextField(max_length=2000, verbose_name='Описание',)
    phone = PhoneNumberField(null=False, blank=False, unique=True,verbose_name='Номер телефона')

    def __str__(self):
        return self.name
