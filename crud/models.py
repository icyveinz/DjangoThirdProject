from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField(
        validators=[MinValueValidator(12), MaxValueValidator(80)]
    )