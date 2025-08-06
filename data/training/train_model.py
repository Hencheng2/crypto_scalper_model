import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

df = pd.read_csv('data/processed/crypto_features.csv')

X = df.drop(columns=['target', 'timestamp'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/model_v1.pkl')
print("Model saved to models/model_v1.pkl")
