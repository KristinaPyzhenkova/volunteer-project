from django.db import models

from projects.models import Project
from users.models import User


class Event(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Наименование события'
    )
    status = models.CharField(
        max_length=256,
        verbose_name='Статус мероприятия'
    )
    avatar_url = models.CharField(
        max_length=256,
        verbose_name='Аватар URL'
    )
    description = models.TextField(
        verbose_name='Описание события'
    )
    date_start = models.DateTimeField(
        verbose_name='Дата начала'
    )
    date_end = models.DateTimeField(
        verbose_name='Дата завершения'
    )
    contact_user = models.ForeignKey(
        User,
        related_name='events',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Контактное лицо'
    )
    project = models.ForeignKey(
        Project,
        related_name='events',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Проект'
    )
    client = models.ManyToManyField(
        User,
        related_name='events_many',
        through='UserEvent',
    )
    slug = models.SlugField(
        unique=True, max_length=50,
        db_index=True, verbose_name='Ссылка события'
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
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name


class Function(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Наименование'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    task = models.TextField(
        verbose_name='Задачи'
    )
    condition = models.TextField(
        verbose_name='Условия'
    )
    event = models.ForeignKey(
        Event,
        related_name='functions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Событие'
    )
    client = models.ManyToManyField(
        User,
        related_name='functions_many',
        through='UserFunction',
    )
    slug = models.SlugField(
        unique=True, max_length=50,
        db_index=True, verbose_name='Ссылка функции'
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
        verbose_name = 'Функции'
        verbose_name_plural = 'Функции'

    def __str__(self):
        return self.name


class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class UserFunction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
