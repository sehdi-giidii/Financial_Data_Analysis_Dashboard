import pandas as pd
import numpy as np

def calculate_daily_returns(data):
    returns = data["Close"].pct_change() * 100
    return returns

def get_close_prices(data):
    Close_Prices = data["Close"]
    return Close_Prices

def calculate_moving_averages(Close_Prices):
    ma_twenty = Close_Prices.rolling(window=20).mean()
    ma_Fifty = Close_Prices.rolling(window=50).mean()
    return ma_twenty, ma_Fifty

def calculate_volatility(returns):
    Volatility = returns.rolling(window=20).std()
    return Volatility


def calculate_cumulative_returns(returns):
    Cumulative_Returns = (1 + returns / 100).cumprod() - 1
    Cumulative_Returns = Cumulative_Returns * 100
    return Cumulative_Returns

def calculate_final_returns(Cumulative_Returns):
    Final_Returns = Cumulative_Returns.iloc[-1]
    return Final_Returns


def calculate_average_returns(returns):
    Average_Returns = returns.mean()
    return Average_Returns

def calculate_daily_volatility(returns):
    Daily_Volatility = returns.std()
    return Daily_Volatility

def create_summary(
    Final_Returns,
    Average_Returns,
    Daily_Volatility
):
    Summary = pd.DataFrame({
        "Cumulative Return (%)": Final_Returns,
        "Average Daily Return (%)": Average_Returns,
        "Daily Volatility (%)": Daily_Volatility
    })
    return Summary