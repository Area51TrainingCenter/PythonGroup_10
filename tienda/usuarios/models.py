from django.db import models

from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    direccion = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    telefono = models.CharField(
        max_length=9,
        blank=False,
        null=False
    )

    dni = models.CharField(
        max_length=8,
        blank=False,
        null=False
    )

    imagen = models.ImageField(
        upload_to='usuarios',
        blank=True,
        null=True
    )
