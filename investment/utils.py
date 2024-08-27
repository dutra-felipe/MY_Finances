import yfinance as yf


def get_stock_info(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    stock_info = stock.info
    return stock_info
