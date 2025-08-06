# streamlit_app/app.py
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Crypto Scalper Signals", layout="wide")
st.title("📈 Crypto Scalper Signals Dashboard")

# Load predictions
def load_predictions():
    path = os.path.join("..", "signals", "predictions.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        return pd.DataFrame()

# Load data
predictions = load_predictions()

if predictions.empty:
    st.warning("No predictions available. Please run the prediction model.")
else:
    coins = predictions['coin'].unique().tolist()
    selected_coin = st.selectbox("Select Cryptocurrency", coins)

    coin_df = predictions[predictions['coin'] == selected_coin].copy()

    st.subheader(f"Latest Prediction for {selected_coin}")
    st.dataframe(coin_df.tail(5).sort_values(by='timestamp', ascending=False), use_container_width=True)

    # Visual summary
    import plotly.express as px
    fig = px.line(coin_df, x='timestamp', y='predicted_close', title=f"Predicted Close Prices - {selected_coin}")
    st.plotly_chart(fig, use_container_width=True)

    st.info("Buy/Sell/TP signals are based on our scalping model targeting small account safety and growth.")
