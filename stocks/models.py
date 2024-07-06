# stocks/models.py

from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10, unique=True)
    latest_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

