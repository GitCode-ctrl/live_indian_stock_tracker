import streamlit as st
import yfinance as yf
import pandas as pd

# Set up the Streamlit page
st.set_page_config(page_title="Live Indian Stock Tracker", layout="centered")
st.title("📈 Real-Time Price Tracker: Top 10 Indian Stocks")

# Define stock symbols
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

# Refresh time selector
refresh_rate = st.slider("⏱ Refresh every (seconds)", 10, 300, 60)

# Auto-refresh using Streamlit's native method
st.experimental_rerun() if st.experimental_get_query_params().get("auto_refresh") else None
st.query_params.st.experimental_set_query_params (auto_refresh="1")

# Fetch function
def fetch_prices():
    data = []
    for name, symbol in top_10_stocks.items():
        stock = yf.Ticker(symbol)
        price = stock.info.get('regularMarketPrice', "N/A")
        data.append({'Stock': name, 'Price (INR)': price})
    return pd.DataFrame(data)

# Display data
df = fetch_prices()
st.table(df)

# Show current time
st.caption(f"Last updated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Auto-refresh using JS workaround
st.markdown(f"""
    <script>
        function refresh() {{
            window.location.reload();
        }}
        setTimeout(refresh, {refresh_rate * 1000});
    </script>
""", unsafe_allow_html=True)
