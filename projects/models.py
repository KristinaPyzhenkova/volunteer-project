from django.db import models
import os

from users.models import User
from live import settings


class Project(models.Model):
    def project_avatar_path(instance, filename):
        ext = filename.split('.')[-1]
        fullname = f'projects/avatars/{instance.pk}.{ext}'
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, fullname)):
            os.remove(os.path.join(settings.MEDIA_ROOT, fullname))
        return f'projects/avatars/{instance.pk}.{ext}'

    name = models.CharField(
        max_length=20,
        verbose_name='Наименование',
        db_index=True
    )
    avatar_url = models.ImageField(
        upload_to=project_avatar_path,
        verbose_name='Аватар'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    goal = models.TextField(
        verbose_name='Цели',
        blank=True,
        null=True
    )
    result = models.TextField(
        verbose_name='Результаты',
        blank=True,
        null=True
    )


    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
