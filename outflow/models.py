from django.db import models
from investment.models import Investment
from django.utils import timezone


class Outflow(models.Model):
    asset = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='outflows')
    quantity = models.IntegerField()
    amount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.asset)
