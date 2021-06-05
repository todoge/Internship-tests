from django import forms
from. models import Result
from django.core import validators
from django.core.validators import MinValueValidator

class RawGuessForm(forms.Form):
    coin = forms.CharField(max_length=120)
    guess_price = forms.DecimalField(decimal_places=2, max_digits=10000, validators=[MinValueValidator(0.01)])