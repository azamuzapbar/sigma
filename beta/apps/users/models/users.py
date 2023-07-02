from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='Фамилия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    username = models.CharField(max_length=250, blank=False, null=False, verbose_name='Логин')
    email = models.EmailField(null=False, blank=False, verbose_name='Почта')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.username
