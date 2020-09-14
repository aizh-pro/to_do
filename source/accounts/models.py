from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user: AbstractUser = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    user_info = models.TextField(null=True, blank=True, verbose_name='О себе')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    profile = models.URLField(null=True, blank=True, verbose_name='Профиль ссылка')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
