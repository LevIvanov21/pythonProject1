from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = dict(null=True, blank=True)


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Электронная почта', help_text='Введите электронную почту')
    phone = models.CharField(max_length=100, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', ]

    def __repr__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk',)
