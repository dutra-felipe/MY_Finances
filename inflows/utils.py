import yfinance as yf
import pandas as pd


def get_stock_price_on_date(symbol, date):
    stock = yf.Ticker(symbol)
    historical_data = stock.history(period='1d', start=date, end=pd.to_datetime(date) + pd.DateOffset(1))

    if not historical_data.empty:
        return historical_data['Close'].iloc[0]
    return None


def get_current_stock_price(symbol):
    stock = yf.Ticker(symbol)
    stock_info = stock.info
    return stock_info['currentPrice']


def calculate_portfolio_valorization(inflows):
    total_initial_value = 0
    total_final_value = 0

    investments = {}

    for inflow in inflows:
        symbol = inflow.asset.symbol
        quantidade = inflow.quantity
        valor_inicial = inflow.amount
        current_price = get_current_stock_price(symbol)

        if symbol not in investments:
            investments[symbol] = {
                'initial': valor_inicial,
                'quantity': quantidade,
                'current_price': current_price
            }
        else:
            investments[symbol]['initial'] += valor_inicial
            investments[symbol]['quantity'] += quantidade
            investments[symbol]['current_price'] = current_price

    for symbol, values in investments.items():
        total_initial_value += values['initial']
        total_final_value += values['quantity'] * values['current_price']

    if total_initial_value > 0:
        total_valorization = ((float(total_final_value) - float(total_initial_value)) / float(total_initial_value)) * 100
    else:
        total_valorization = 0

    return round(total_valorization, 2)
