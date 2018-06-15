from django.db import models


class Producto(models.Model):
    nombre = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )

    precio = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=False,
        null=False
    )

    descripcion = models.TextField(
        blank=False,
        null=False
    )

    stock = models.IntegerField(
        default=0,
        blank=False,
        null=False
    )

    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    # - imágenes
    # - calificación

    def __str__(self):
        return self.nombre


class Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    imagen = models.ImageField(
        upload_to='productos',
        blank=False,
        null=False
    )


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nombre
