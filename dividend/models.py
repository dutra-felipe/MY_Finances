from django.db import models
from investment.models import Investment
from .utils import get_stock_dividends


class Dividend(models.Model):
    name = models.ForeignKey(Investment, on_delete=models.CASCADE)
    total_dividends = models.FloatField()

    class Meta:
        ordering = ['name']

    def dividends_per_share(self):
        ticker_symbol = self.name.symbol
        dividends = get_stock_dividends(ticker_symbol)
        return dividends

    def __str__(self):
        return self.name.name
