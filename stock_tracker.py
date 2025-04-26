import streamlit as st
import yfinance as yf
import pandas as pd
import time

# Set up page
st.set_page_config(page_title="Top 10 Indian Stocks", layout="centered")
st.title("📈 Live Price Tracker: Top 10 Indian Stocks")

# Stock list
top_10_stocks = {
    'RELIANCE': 'RELIANCE.NS',
    'TCS': 'TCS.NS',
    'HDFCBANK': 'HDFCBANK.NS',
    'INFY': 'INFY.NS',
    'ICICIBANK': 'ICICIBANK.NS',
    'HINDUNILVR': 'HINDUNILVR.NS',
    'SBIN': 'SBIN.NS',
    'BHARTIARTL': 'BHARTIARTL.NS',
    'KOTAKBANK': 'KOTAKBANK.NS',
    'ITC': 'ITC.NS'
}

# Function to get prices
def fetch_prices():
    data = []
    for name, symbol in top_10_stocks.items():
        try:
            stock = yf.Ticker(symbol)
            price = stock.info.get('regularMarketPrice', 'N/A')
        except:
            price = 'N/A'
        data.append({'Stock': name, 'Price (INR)': price})
    return pd.DataFrame(data)

# Slider to control refresh interval
refresh_interval = st.slider("🔁 Refresh every (seconds)", 10, 300, 60)

# Button to manually refresh
if st.button("🔄 Refresh Now"):
    df = fetch_prices()
    st.table(df)
    st.caption(f"Last updated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
else:
    df = fetch_prices()
    st.table(df)
    st.caption(f"Auto-refreshed at: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Auto-refresh using HTML/JS
st.markdown(f"""
    <script>
        setTimeout(function(){{
            window.location.reload();
        }}, {refresh_interval * 1000});
    </script>
""", unsafe_allow_html=True)
