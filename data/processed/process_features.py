import pandas as pd
import ta
import os

def load_and_engineer(file_path, coin_name):
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['Date'] if 'Date' in df else df['Datetime'])
    df = df[['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']].dropna()

    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    macd = ta.trend.MACD(df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    df['SMA_20'] = ta.trend.SMAIndicator(df['Close'], window=20).sma_indicator()
    df['EMA_20'] = ta.trend.EMAIndicator(df['Close'], window=20).ema_indicator()
    df['BB_High'] = ta.volatility.BollingerBands(df['Close']).bollinger_hband()
    df['BB_Low'] = ta.volatility.BollingerBands(df['Close']).bollinger_lband()

    df = df.dropna()
    df['coin'] = coin_name

    return df

files = {
    'data/raw/bitcoin.csv': 'BTC',
    'data/raw/ethereum.csv': 'ETH',
    'data/raw/litecoin.csv': 'LTC'
}

all_df = []
for file_path, name in files.items():
    if os.path.exists(file_path):
        df = load_and_engineer(file_path, name)
        all_df.append(df)

full_df = pd.concat(all_df)
os.makedirs('data/processed', exist_ok=True)
full_df.to_csv('data/processed/crypto_features.csv', index=False)
print("Processed data with indicators saved.")
