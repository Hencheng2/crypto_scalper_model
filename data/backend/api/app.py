# backend/api/app.py
from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

PREDICTIONS_PATH = os.path.join("..", "signals", "predictions.csv")

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Crypto Scalper Prediction API"})

@app.route('/predictions', methods=['GET'])
def get_predictions():
    if not os.path.exists(PREDICTIONS_PATH):
        return jsonify({"error": "Predictions file not found."}), 404

    df = pd.read_csv(PREDICTIONS_PATH)
    coin = request.args.get("coin")

    if coin:
        df = df[df['coin'].str.lower() == coin.lower()]

    return jsonify(df.tail(50).to_dict(orient="records"))

@app.route('/prediction/latest', methods=['GET'])
def get_latest():
    if not os.path.exists(PREDICTIONS_PATH):
        return jsonify({"error": "Predictions file not found."}), 404

    df = pd.read_csv(PREDICTIONS_PATH)
    coin = request.args.get("coin")
    if coin:
        df = df[df['coin'].str.lower() == coin.lower()]

    latest = df.sort_values(by='timestamp', ascending=False).head(1)
    return jsonify(latest.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
