from django.db import models

from Stock.models import Stock
from User.models import User


# Create your models here.
class Transaction(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(null=True)
    quantity = models.IntegerField()
    type = models.CharField(max_length=16)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class UserStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
