from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    direccion = forms.CharField(
        max_length=255,
        required=True,
        label='Dirección'
    )

    telefono = forms.CharField(
        max_length=9,
        min_length=9,
        required=True,
        label='Teléfono'
    )

    dni = forms.CharField(
        max_length=8,
        min_length=8,
        required=True,
        label='DNI'
    )
