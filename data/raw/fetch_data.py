import yfinance as yf
import pandas as pd
import os

symbols = {
    'BTC-USD': 'bitcoin',
    'ETH-USD': 'ethereum',
    'LTC-USD': 'litecoin'
}

os.makedirs('data/raw', exist_ok=True)

for symbol, name in symbols.items():
    df = yf.download(symbol, start='2020-01-01', interval='1h')
    df.to_csv(f'data/raw/{name}.csv')
    print(f"{name} data saved.")
