from django.db import models
from django.contrib.auth.models import AbstractUser


class UserGender(models.TextChoices):
    MALE = "Masculino"
    FEMALE = "Feminino"
    OTHERS = "Outros"
    DEFAULT = "Não definido"


class User(AbstractUser):
    email = models.EmailField(
        max_length=127,
        unique=True,
        error_messages={"unique": "This field must be unique."},
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    gender = models.CharField(
        max_length=20,
        choices=UserGender.choices,
        default=UserGender.DEFAULT,
    )
