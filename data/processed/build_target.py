import pandas as pd

df = pd.read_csv('data/processed/crypto_features.csv')

future_steps = 3
threshold = 0.01

df['Future_Close'] = df['Close'].shift(-future_steps)
df['Price_Change'] = (df['Future_Close'] - df['Close']) / df['Close']
df['target'] = pd.cut(df['Price_Change'], bins=[-float('inf'), -threshold, threshold, float('inf')], labels=[-1, 0, 1]).astype(int)

df.drop(columns=['Future_Close', 'Price_Change'], inplace=True)
df.to_csv('data/processed/crypto_features.csv', index=False)
print("Target column added.")
