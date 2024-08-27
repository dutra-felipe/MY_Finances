from investment.models import Investment
from inflows import models
from inflows.utils import calculate_portfolio_valorization
from dividend.utils import get_total_dividends
from django.utils import timezone
from inflows.models import Inflow
from django.db.models import Sum
from django.core.cache import cache
from type.models import Type


inflows = models.Inflow.objects.all()


def get_investment_metrics():
    investments = Investment.objects.all()
    total_quantity = sum(investment.quantity for investment in investments)
    wallet_amount = sum(investment.amount for investment in investments)
    valorization = calculate_portfolio_valorization(inflows)
    dividends = round(get_total_dividends(), 2)

    return {
        "total_quantity": total_quantity,
        "wallet_amount": wallet_amount,
        "valorization": valorization,
        "dividends": dividends
    }


def get_portfolio_valorization_data():
    cache_key = "portfolio_valorization_data"
    cached_data = cache.get(cache_key)

    if cached_data:
        return cached_data

    first_inflow = Inflow.objects.order_by('created_at').first()
    if not first_inflow:
        return dict(dates=[], values=[])

    start_date = first_inflow.created_at
    end_date = timezone.now().date()
    dates = []
    values = []

    current_date = start_date

    while current_date <= end_date:
        next_date = current_date + timezone.timedelta(days=30)
        inflows = Inflow.objects.filter(created_at__lte=next_date)
        monthly_valorization = calculate_portfolio_valorization(inflows) if inflows else 0

        dates.append(current_date.strftime("%Y-%m"))
        values.append(float(monthly_valorization))

        current_date = next_date

    valorization_data = dict(
        dates=dates,
        values=values,
    )

    # Salva os dados no cache por 7 dias
    cache.set(cache_key, valorization_data, timeout=604800)

    return valorization_data


def get_daily_investment_amount_data():
    first_inflow = Inflow.objects.order_by('created_at').first()
    if not first_inflow:
        return dict(dates=[], values=[])

    start_date = first_inflow.created_at.replace(day=1)
    end_date = timezone.now().date().replace(day=1)

    dates = []
    values = []

    current_date = start_date
    accumulated_value = 0

    while current_date <= end_date:
        monthly_total_amount = Inflow.objects.filter(
            created_at__year=current_date.year,
            created_at__month=current_date.month
        ).aggregate(total_amount=Sum('amount'))['total_amount'] or 0

        accumulated_value += float(monthly_total_amount)

        dates.append(current_date.strftime("%Y-%m"))
        values.append(accumulated_value)

        current_date = (current_date + timezone.timedelta(days=32)).replace(day=1)

    return dict(
        dates=dates,
        values=values,
    )


def get_wallet_division():
    types = Type.objects.all()
    return {type_obj.name: Investment.objects.filter(investment_type=type_obj).count() for type_obj in types}


def get_wallet_allocation():
    # Obtém a quantidade total para cada ativo
    asset_quantities = Investment.objects.values('symbol').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')

    # Cria um dicionário com o símbolo do ativo e a quantidade total
    allocation = {asset['symbol']: asset['total_quantity'] for asset in asset_quantities}

    return allocation
