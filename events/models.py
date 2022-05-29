from django.db import models
import os

from projects.models import Project
from users.models import User
from live import settings


class Event(models.Model):
    def event_avatar_path(instance, filename):
        ext = filename.split('.')[-1]
        fullname = f'events/avatars/{instance.pk}.{ext}'
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, fullname)):
            os.remove(os.path.join(settings.MEDIA_ROOT, fullname))
        return f'events/avatars/{instance.pk}.{ext}'

    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Наименование события'
    )
    status = models.CharField(
        max_length=256,
        verbose_name='Местоположение'
    )
    avatar_url = models.ImageField(
        upload_to=event_avatar_path,
        verbose_name='Аватар мероприятия'
    )
    description = models.TextField(
        verbose_name='Описание события',
        blank=True
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
        on_delete=models.CASCADE,
        verbose_name='Контактное лицо'
    )
    project = models.ForeignKey(
        Project,
        related_name='events',
        on_delete=models.SET_NULL,
        verbose_name='Проект',
        null=True
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
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    count = models.IntegerField(
        default=0,
        verbose_name='Нужное кол-во волонтеров'
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


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='подписчик',
        help_text='ссылка на объект пользователя, который подписывается',
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='following',
    )
    function = models.ForeignKey(
        Function,
        on_delete=models.CASCADE,
        related_name='following',
    )

class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='подписчик',
        help_text='ссылка на объект пользователя, который подписывается',
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='favorites',
        help_text='событие',
    )

