import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

stocks = ["GOOG", "AAPL", "MSFT"]

data = yf.download(
    stocks,
    start="2020-01-01",
    end="2026-01-01",
    interval="1d"
)

# This is just for info about returns
returns= (data["Close"].pct_change() * 100)
print(returns.describe())

# Only using Closing prices
Close_Prices = data["Close"]
print(Close_Prices.head())

# Average of 20days
ma_twenty= Close_Prices.rolling(window= 20).mean()
print(ma_twenty.head(25))

# Average of 50 days
ma_Fifty= Close_Prices.rolling(window=50).mean()
print(ma_Fifty.head(55))

# print(ma_twenty.tail())
# print(ma_Fifty.tail())


# Calculating Volatality for 20 days now lets see
Volatility= returns.rolling(window=20).std()
print(Volatility.tail())


# Now Calculating cumulative returns
Cumulative_Returns = (1 + returns / 100).cumprod() - 1
Cumulative_Returns = Cumulative_Returns * 100
print(Cumulative_Returns.tail())


# Now checking the final returns
Final_Returns= Cumulative_Returns.iloc[-1]
print(Final_Returns)
print(Final_Returns.sort_values(ascending=False))




# REMEMBER THE MATPLOTLIB AUTOMATICALLY USES THE INDEX OF X AXIS AND THE VALUES FOR THE Y AXIS
# plt.figure(figsize= (12,6))
# plt.plot(Close_Prices["AAPL"], label= "Apple", color= "orange", linewidth = 2, linestyle= "-")
# plt.plot(Close_Prices["GOOG"], label= "Google", color= "green", linewidth= 2)
# plt.plot(Close_Prices["MSFT"], label= "Microsoft", color= "blue", linewidth= 2, linestyle= "-.")
#
#
# plt.title("Historical Closing Prices of Stock", fontsize= 20)
# plt.xlabel("Date", fontsize= 14)
# plt.ylabel("Closing Price", fontsize= 14)
#
# plt.legend(loc= "upper left", fontsize= 12)
# plt.grid(axis= "y", alpha=0.3)
#
# plt.tight_layout()
# plt.show()
#
#
#
#
#
# plt.figure(figsize=(14, 7))
# plt.plot(Close_Prices["AAPL"], label="Actual Price", color="blue", linewidth=1)
# plt.plot(ma_twenty["AAPL"], label="20-Day MA", color="orange", linewidth=1.5)
# plt.plot(ma_Fifty["AAPL"], label="50-Day MA", color="red", linewidth=1.5)
#
# plt.title("Apple Stock Price with Moving Averages", fontsize=16)
# plt.xlabel("Date")
# plt.ylabel("Closing Price (USD)")
#
# plt.legend()
# plt.grid(axis="y", alpha=0.3)
#
# plt.tight_layout()
# plt.show()
#
#
#
#
#
# plt.figure(figsize=(14, 7))
# plt.plot(Close_Prices["GOOG"], label="Actual Price", color="blue", linewidth=1)
# plt.plot(ma_twenty["GOOG"], label="20-Day MA", color="orange", linewidth=1.5)
# plt.plot(ma_Fifty["GOOG"], label="50-Day MA", color="red", linewidth=1.5)
#
# plt.title("Google Stock Price with Moving Averages", fontsize=16)
# plt.xlabel("Date")
# plt.ylabel("Closing Price (USD)")
#
# plt.legend()
# plt.grid(axis="y", alpha=0.3)
#
# plt.tight_layout()
# plt.show()
#
#
#
#
#
#
#
# plt.figure(figsize=(14, 7))
# plt.plot(Close_Prices["MSFT"], label="Actual Price", color="blue", linewidth=1)
# plt.plot(ma_twenty["MSFT"], label="20-Day MA", color="orange", linewidth=1.5)
# plt.plot(ma_Fifty["MSFT"], label="50-Day MA", color="red", linewidth=1.5)
#
# plt.title("Microsoft Stock Price with Moving Averages", fontsize=16)
# plt.xlabel("Date")
# plt.ylabel("Closing Price (USD)")
#
# plt.legend()
# plt.grid(axis="y", alpha=0.3)
#
# plt.tight_layout()
# plt.show()
#
#
#
#
#
# all_returns = returns.to_numpy().flatten()
# all_returns = all_returns[~np.isnan(all_returns)]
#
#
# bins = np.linspace(all_returns.min(), all_returns.max(), 51)
#
# plt.figure(figsize=(12, 6))
#
# plt.hist(returns["AAPL"].dropna(), bins=bins, histtype="step",
#          linewidth=1.8, label="Apple")
#
# plt.hist(returns["GOOG"].dropna(), bins=bins, histtype="step",
#          linewidth=1.8, label="Google")
#
# plt.hist(returns["MSFT"].dropna(), bins=bins, histtype="step",
#          linewidth=1.8, label="Microsoft")
#
# plt.title("Daily Returns Distribution Comparison", fontsize=16)
# plt.xlabel("Daily Returns (%)")
# plt.ylabel("Frequency")
#
# plt.axvline(x=0, color="black", linestyle="--", alpha=0.5)
#
# plt.legend()
# plt.grid(axis="y", alpha=0.3)
# plt.tight_layout()
# plt.show()
#
#
#
#
# volume = data["Volume"]
# plt.figure(figsize=(14, 7))
#
# plt.plot(volume["AAPL"]/1e6, label="Apple", linewidth=1)
# plt.plot(volume["GOOG"]/1e6, label="Google", linewidth=1)
# plt.plot(volume["MSFT"]/1e6, label="Microsoft", linewidth=1)
#
# plt.title("Daily Trading Volume Comparison (2020-2025)", fontsize=16)
# plt.xlabel("Date")
# plt.ylabel("Trading Volume (Millions of Shares)")
#
# plt.legend()
# plt.grid(axis="y", alpha=0.3)
#
# plt.tight_layout()
# plt.show()
#
#
#
#
#
#
#
# plt.figure(figsize=(14, 7))
#
# plt.plot(Cumulative_Returns["AAPL"], label="Apple", linewidth=2)
# plt.plot(Cumulative_Returns["GOOG"], label="Google", linewidth=2)
# plt.plot(Cumulative_Returns["MSFT"], label="Microsoft", linewidth=2)
#
# plt.title("Cumulative Returns Comparison (2020-2025)", fontsize=16)
# plt.xlabel("Date")
# plt.ylabel("Cumulative Returns (%)")
#
# plt.axhline(y=0, color="black", linestyle="--", alpha=0.5)
#
# plt.legend()
# plt.grid(axis="y", alpha=0.3)
#
# plt.tight_layout()
# plt.show()
#
#
#
#
#
#
#
#
#
# plt.figure(figsize=(14, 7))
#
# plt.plot(Volatility["AAPL"], label="Apple", linewidth=1)
# plt.plot(Volatility["GOOG"], label="Google", linewidth=1)
# plt.plot(Volatility["MSFT"], label="Microsoft", linewidth=1)
#
# plt.title("20-Day Rolling Volatility Comparison", fontsize=16)
# plt.xlabel("Date")
# plt.ylabel("Volatility (Standard Deviation of Daily Returns %)")
#
# plt.legend()
# plt.grid(axis="y", alpha=0.3)
#
# plt.tight_layout()
# plt.show()







print(Final_Returns.sort_values(ascending=False))
Average_Returns = returns.mean()

print("Average Daily Returns:")
print(Average_Returns.sort_values(ascending=False))

Daily_Volatility = returns.std()
print("Daily Volatility:")
print(Daily_Volatility.sort_values(ascending=False))


Summary = pd.DataFrame({
    "Cumulative Return (%)": Final_Returns,
    "Average Daily Return (%)": Average_Returns,
    "Daily Volatility (%)": Daily_Volatility
})
print(Summary.sort_values(
    by="Cumulative Return (%)",
    ascending=False
))