from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ResultManager(models.Manager):
    def create_result(self, coin, guess_price, actual_price, author):
        coin = self.create(coin=coin, guess_price=guess_price, actual_price=actual_price, author=author);
        return coin

class Result(models.Model):
    coin = models.CharField(max_length=120, blank=False, null=False)
    guess_price = models.DecimalField(decimal_places=2, max_digits=10000)
    actual_price = models.DecimalField(decimal_places=2, max_digits=10000)
    author = models.ForeignKey(User, related_name='result', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ResultManager()

    def __str__(self):
        return f"{self.coin}: guess {self.guess_price} actual {self.actual_price}"

