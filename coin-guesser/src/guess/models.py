from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Guess(models.Model):
    coin = models.CharField(max_length=120, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10000, validators=[MinValueValidator(0.01)])
