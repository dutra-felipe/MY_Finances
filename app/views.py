import json
from django.shortcuts import render
from . import metrics


def home(request):
    investment_metrics = metrics.get_investment_metrics()
    valorization_data = metrics.get_portfolio_valorization_data()
    amount_data = metrics.get_daily_investment_amount_data()
    wallet_division = metrics.get_wallet_division()
    wallet_allocation = metrics.get_wallet_allocation()

    context = {
        'investment_metrics': investment_metrics,
        'daily_valorization_data': json.dumps(valorization_data),
        'amount_data': json.dumps(amount_data),
        'wallet_division': json.dumps(wallet_division),
        'wallet_allocation': json.dumps(wallet_allocation),
    }

    return render(request, 'home.html', context)
