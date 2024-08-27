from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from outflow.models import Outflow
from dividend.models import Dividend
from dividend.utils import get_stock_dividends
from investment.models import Investment
from django.core.cache import cache
from inflows.utils import calculate_portfolio_valorization


@receiver(post_save, sender=Outflow)
def update_invest_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            investment = instance.asset
            investment.quantity -= instance.quantity
            investment.save()


@receiver(post_save, sender=Outflow)
def update_invest_amount(sender, instance, created, **kwargs):
    if created:
        if instance.amount > 0:
            investment = instance.asset
            investment.amount -= instance.amount
            investment.save()


@receiver(post_save, sender=Outflow)
def update_dividends_on_outflow(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            investment = instance.asset

            dividends = Dividend.objects.filter(name=investment)

            for dividend in dividends:
                dividends_per_share = get_stock_dividends(dividend.name.symbol)
                total_dividends = dividends_per_share * investment.quantity
                dividend.total_dividends = total_dividends
                dividend.save()


@receiver(post_delete, sender=Outflow)
def update_inventory_on_delete(sender, instance, **kwargs):
    inventory = Investment.objects.get(name=instance.asset)

    inventory.quantity += instance.quantity
    inventory.amount += instance.amount

    if inventory.quantity <= 0:
        inventory.quantity = 0
        inventory.amount = 0
    inventory.save()


@receiver(post_delete, sender=Outflow)
def update_dividends_on_delete(sender, instance, **kwargs):
    investment = Investment.objects.get(name=instance.asset)

    dividends = Dividend.objects.filter(name=investment)

    for dividend in dividends:
        dividends_per_share = get_stock_dividends(dividend.name.symbol)
        total_dividends = dividends_per_share * investment.quantity
        dividend.total_dividends = total_dividends
        dividend.save()

    if investment.quantity <= 0:
        investment.quantity = 0
        investment.amount = 0
    investment.save()


@receiver(post_save, sender=Outflow)
def reset_valorization_cache(sender, instance, **kwargs):
    cache_key = "portfolio_valorization_data"
    cache.delete(cache_key)


@receiver(post_delete, sender=Outflow)
def recalculate_portfolio_valorization_on_delete(sender, instance, **kwargs):
    Outflows = Outflow.objects.all()
    new_total_valorization = calculate_portfolio_valorization(Outflows)

    cache.set('total_portfolio_valorization', new_total_valorization)


@receiver(post_save, sender=Outflow)
def delete_investment_if_zero_quantity(sender, instance, created, **kwargs):
    if created:
        investment = instance.asset
        if investment.quantity <= 0:
            investment.delete()
