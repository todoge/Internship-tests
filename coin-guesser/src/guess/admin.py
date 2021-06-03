from django.contrib import admin

# Register your models here.
from .models import Guess

admin.site.register(Guess)