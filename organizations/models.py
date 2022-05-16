from django.db import models

from users.models import User


class Organization(models.Model):

    full_name = models.CharField(
        max_length=256,
        verbose_name='Полное наименование'
    )
    name = models.CharField(
        max_length=256,
        verbose_name='Наименование'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    email = models.EmailField(
        max_length=256,
        verbose_name='Электронная почта'
    )
    address = models.CharField(
        max_length=256,
        verbose_name='Адрес'
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Телефон'
    )
    avatar_url = models.CharField(
        max_length=256,
        verbose_name='Аватар URL'
    )
    website = models.CharField(
        max_length=256,
        verbose_name='Сайт Организации'
    )
    legal_form = models.CharField(
        max_length=256,
        verbose_name='Организационно-правовая форма',
        db_index=True
    )
    leader = models.ForeignKey(
        User,
        related_name='organizations',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Руководитель'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        verbose_name = 'Организации'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name
