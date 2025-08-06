import pandas as pd
from strategies.scalping_strategy import generate_signals

df = pd.read_csv('data/processed/crypto_features.csv')
df = generate_signals(df)

initial_balance = 1000
balance = initial_balance
position = 0
entry_price = 0

for i, row in df.iterrows():
    signal = row['Signal']
    price = row['Close']

    if signal == 'Buy' and position == 0:
        entry_price = price
        position = 1
    elif signal == 'Sell' and position == 1:
        profit = price - entry_price
        balance += profit
        position = 0

print(f"Initial balance: {initial_balance}")
print(f"Final balance: {balance}")
