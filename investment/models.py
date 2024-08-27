from django.db import models
from type.models import Type


class Investment(models.Model):
    name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=20)
    investment_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    operation = models.CharField(max_length=10, choices=[('buy', 'Compra'), ('sell', 'Venda')])
    amount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
