from django.core.cache import cache
import yfinance as yf
from datetime import datetime
from django.db.models import Sum


def get_stock_dividends(ticker_symbol):
    cache_key = f"dividends_{ticker_symbol}"
    dividends = cache.get(cache_key)

    if dividends is None:
        stock = yf.Ticker(ticker_symbol)
        dividends = stock.dividends
        if not dividends.empty:
            cache.set(cache_key, dividends, timeout=86400)

    if not dividends.empty:
        latest_dividend = dividends.iloc[-1]
        return float(latest_dividend)
    return 0.0


def convert_unix_timestamp(timestamp):
    """
    Converte uma timestamp Unix em uma string de data legível.
    """
    if timestamp:
        date = datetime.fromtimestamp(timestamp)
        return date.strftime('%Y-%m-%d %H:%M:%S')
    return 'Data não disponível'


def get_total_dividends():
    from .models import Dividend
    total_dividends = Dividend.objects.aggregate(total_sum=Sum('total_dividends'))['total_sum']
    return total_dividends or 0
