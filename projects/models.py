from django.db import models

from organizations.models import Organization
from users.models import User


class Project(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Наименование',
        # для ускоренной сортировки
        db_index=True
    )
    full_name = models.CharField(
        max_length=256,
        verbose_name='Полное наименование',
        db_index=True
    )
    website = models.CharField(
        max_length=256,
        verbose_name='Сайт Проекта',
        db_index=True
    )
    material_url = models.CharField(
        max_length=256,
        verbose_name='Материал',
        blank=True
    )
    avatar_url = models.CharField(
        max_length=256,
        verbose_name='Аватар URL',
        blank=True
    )
    status = models.CharField(
        max_length=256,
        verbose_name='Статус проекта',
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    goal = models.TextField(
        verbose_name='Цели',
        blank=True
    )
    result = models.TextField(
        verbose_name='Результаты',
        blank=True
    )
    slug = models.SlugField(
        unique=True, max_length=50,
        db_index=True, verbose_name='Ссылка проекта'
    )
    organization = models.ForeignKey(
        Organization,
        related_name='projects',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Организация'
    )
    client = models.ManyToManyField(
        User,
        related_name='projects_many',
        through='UserProject',
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
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
