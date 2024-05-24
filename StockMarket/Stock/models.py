from django.db import models


# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=32, unique=True)
    co_name = models.CharField(max_length=64, unique=True)
    last_price = models.FloatField()
    change = models.FloatField(null=True)
