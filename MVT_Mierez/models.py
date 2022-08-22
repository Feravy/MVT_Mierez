from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(105),
            MinValueValidator(1)
        ]
    )