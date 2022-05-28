import os

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models

from live import settings


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, date_birthday, gender, **extra_fields):
        if not email:
            raise ValueError('Не заполненое поле Email')
        if not first_name:
            raise ValueError('Не заполненое поле Имя')
        if not last_name:
            raise ValueError('Не заполненое поле Фамилия')
        if not date_birthday:
            raise ValueError('Не заполненое поле Дата рождения')
        if not gender:
            raise ValueError('Не заполненое поле Пол')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, date_birthday=date_birthday,
                          gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, date_birthday, gender, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email, first_name, last_name, password, date_birthday, gender, **extra_fields
        )

    def create_superuser(self, email, first_name, last_name, date_birthday, gender, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')
        return self._create_user(
            email, first_name, last_name, password, date_birthday, gender, **extra_fields
        )


class Direction(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Наименование',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Направления'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):

    def user_avatar_path(instance, filename):
        ext = filename.split('.')[-1]
        fullname = f'users/avatars/{instance.pk}.{ext}'
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, fullname)):
            os.remove(os.path.join(settings.MEDIA_ROOT, fullname))
        return f'users/avatars/{instance.pk}.{ext}'

    VOLUNTEER = 'Волонтер'
    ORGANIZER = 'Организатор'
    STATUS_CHOICES = [
        (VOLUNTEER, 'Волонтер'),
        (ORGANIZER, 'Организатор'),
    ]

    MALE = 'Мужской'
    FEMALE = 'Женский'
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]

    email = models.EmailField(
        max_length=256,
        unique=True,
        verbose_name='Электронная почта'
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Фамилия'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Персонал'
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    date_birthday = models.DateField(
        verbose_name='Дата рождения'
    )
    gender = models.CharField(
        max_length=7,
        choices=GENDER_CHOICES,
        verbose_name='Пол'
    )
    info = models.TextField(
        null=True,
        blank=True,
        verbose_name='Личная информация'
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name='Телефон'
    )
    telegram_url = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='Telegram URL'
    )
    vk_url = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='VK URL'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=VOLUNTEER,
        verbose_name='Статус'
    )
    avatar = models.ImageField(
        upload_to=user_avatar_path,
        default='users/avatars/profile.png',
        verbose_name='Аватар'
    )
    direction = models.ManyToManyField(
        Direction,
        related_name='users_direction',
        through='UserDirection',
        verbose_name='Направления'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_birthday', 'gender']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.get_full_name()} <{self.email}>'


class UserDirection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'UserDirection'
        verbose_name_plural = 'UserDirection'


class Certificate(models.Model):
    url = models.CharField(
        max_length=256,
        verbose_name='Сертификат URL',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='certificates'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Сертификаты'
        verbose_name_plural = 'Сертификаты'


class ReviewUser(models.Model):
    volunteer = models.ForeignKey(
        User,
        related_name='reviews_user',
        on_delete=models.CASCADE,
        verbose_name='Волонтер'
    )
    organization = models.ForeignKey(
        'organizations.Organization',
        related_name='reviews_user',
        on_delete=models.CASCADE,
        verbose_name='Организация'
    )
    event = models.ForeignKey(
        'events.Event',
        related_name='reviews_user',
        on_delete=models.CASCADE,
        verbose_name='Мероприятие'
    )
    review = models.TextField(
        verbose_name='Отзыв'
    )
    rating = models.FloatField(
        verbose_name='Рейтинг'
    )
    created = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
