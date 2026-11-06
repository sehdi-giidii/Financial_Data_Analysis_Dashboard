import yfinance as yf
import streamlit as st

@st.cache_data(ttl=3600)
def download_stock_data():

    stocks = ["GOOG", "AAPL", "MSFT"]

    data = yf.download(
        stocks,
        start="2020-01-01",
        end="2026-01-01",
        interval="1d"
    )

    return data