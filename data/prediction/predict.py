import pandas as pd
import joblib

model = joblib.load('models/model_v1.pkl')
df = pd.read_csv('data/processed/new_crypto_data.csv')

X = df.drop(columns=['timestamp'])
predictions = model.predict(X)
df['Predicted_Signal'] = predictions

df.to_csv('signals/predictions.csv', index=False)
print("Predictions saved to signals/predictions.csv")
