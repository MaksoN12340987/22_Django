from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


class BaseUser(AbstractUser):
    # Поля модели по умолчанию:
    # "id"
    # "last_login"
    # "is_superuser" - Обозначает, что этот пользователь имеет все разрешения,
    #                  не назначая их явно.
    # "username"
    # "first_name"
    # "last_name"
    # "is_staff" - Определяет, может ли пользователь войти на этот сайт как администратор.
    # "is_active"
    # "date_joined"
    # "groups" - Группы, к которым принадлежит этот пользователь.
    #           Пользователь получит все разрешения, предоставленные каждой из его групп
    # "user_permissions" - Конкретные разрешения для этого пользователя
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email
