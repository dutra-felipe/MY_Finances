from django.db.models.signals import post_save
from django.dispatch import receiver
from investment.models import Investment
from dividend.models import Dividend


@receiver(post_save, sender=Investment)
def create_dividend(sender, instance, created, **kwargs):
    if created:
        Dividend.objects.create(
            name=instance,
            total_dividends=0,
        )
