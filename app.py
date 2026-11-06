
import streamlit as st

from data import download_stock_data

from analysis import (
    calculate_daily_returns,
    get_close_prices,
    calculate_moving_averages,
    calculate_volatility,
    calculate_cumulative_returns,
    calculate_final_returns,
    calculate_average_returns,
    calculate_daily_volatility,
    create_summary
)

from charts import (
    plot_closing_prices,
    plot_moving_averages,
    plot_returns_distribution,
    plot_trading_volume,
    plot_cumulative_returns,
    plot_volatility
)


st.set_page_config(
    page_title="Financial Dashboard",
    layout="wide"
)


def display_chart(chart_function, *args):
    left, center, right = st.columns([2, 6, 2])

    with center:
        fig = chart_function(*args)
        st.pyplot(fig, use_container_width=True)


def display_small_chart(chart_function, *args):
    fig = chart_function(*args)
    st.pyplot(fig, use_container_width=True)

data = download_stock_data()

returns = calculate_daily_returns(data)

Close_Prices = get_close_prices(data)

ma_twenty, ma_Fifty = calculate_moving_averages(Close_Prices)

Volatility = calculate_volatility(returns)

Cumulative_Returns = calculate_cumulative_returns(returns)

Final_Returns = calculate_final_returns(Cumulative_Returns)

Average_Returns = calculate_average_returns(returns)

Daily_Volatility = calculate_daily_volatility(returns)

Summary = create_summary(
    Final_Returns,
    Average_Returns,
    Daily_Volatility
)

volume = data["Volume"]


st.title("Financial Data Analysis Dashboard")

st.write(
    "An analysis of Apple, Google and Microsoft "
    "stock performance from Jan-1-2020 to Jan-1-2026."
)


selected_stocks = st.multiselect(
    "Select companies to compare:",
    options=["AAPL", "GOOG", "MSFT"],
    default=["AAPL", "GOOG", "MSFT"]
)


st.subheader("Stock Performance Summary")

if selected_stocks:
    columns = st.columns(len(selected_stocks))

    for i, stock in enumerate(selected_stocks):
        with columns[i]:
            st.markdown(f"### {stock}")

            st.metric(
                label="Cumulative Return",
                value=f"{Summary.loc[stock, 'Cumulative Return (%)']:.2f}%"
            )

            st.metric(
                label="Average Daily Return",
                value=f"{Summary.loc[stock, 'Average Daily Return (%)']:.3f}%"
            )

            st.metric(
                label="Daily Volatility",
                value=f"{Summary.loc[stock, 'Daily Volatility (%)']:.3f}%"
            )
else:
    st.info("Please select at least one company.")


st.subheader("Historical Stock Price Comparison")

if selected_stocks:
    display_chart(
        plot_closing_prices,
        Close_Prices,
        selected_stocks
    )


st.subheader("Moving Averages Comparison")

if selected_stocks:
    display_chart(
        plot_moving_averages,
        Close_Prices,
        ma_twenty,
        ma_Fifty,
        selected_stocks
    )


col1, col2 = st.columns(2)

with col1:
    st.subheader("Daily Returns Distribution")

    if selected_stocks:
        display_small_chart(
            plot_returns_distribution,
            returns,
            selected_stocks
        )

with col2:
    st.subheader("Daily Trading Volume")

    if selected_stocks:
        display_small_chart(
            plot_trading_volume,
            volume,
            selected_stocks
        )


col1, col2 = st.columns(2)

with col1:
    st.subheader("Cumulative Returns")

    if selected_stocks:
        display_small_chart(
            plot_cumulative_returns,
            Cumulative_Returns,
            selected_stocks
        )

with col2:
    st.subheader("20-Day Rolling Volatility")

    if selected_stocks:
        display_small_chart(
            plot_volatility,
            Volatility,
            selected_stocks
        )


st.subheader("Key Findings")

if selected_stocks:
    selected_Summary = Summary.loc[selected_stocks]

    best_return_stock = selected_Summary[
        "Cumulative Return (%)"
    ].idxmax()

    lowest_volatility_stock = selected_Summary[
        "Daily Volatility (%)"
    ].idxmin()

    highest_average_return = selected_Summary[
        "Average Daily Return (%)"
    ].idxmax()

    st.write(f"📈 **Highest Cumulative Return:** {best_return_stock}")

    st.write(f"📉 **Lowest Daily Volatility:** {lowest_volatility_stock}")

    st.write(f"💹 **Highest Average Daily Return:** {highest_average_return}")
