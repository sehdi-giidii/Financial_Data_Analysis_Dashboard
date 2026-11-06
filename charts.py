
import matplotlib.pyplot as plt
import numpy as np


colors = {
    "AAPL": "#F59E0B",
    "GOOG": "#3B82F6",
    "MSFT": "#10B981"
}


def plot_closing_prices(Close_Prices, selected_stocks):

    fig, ax = plt.subplots(figsize=(12, 6))

    for stock in selected_stocks:
        ax.plot(
            Close_Prices[stock],
            label=stock,
            color=colors[stock],
            linewidth=2
        )

    ax.set_title("Historical Closing Prices of Stocks", fontsize=18)
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price (USD)")

    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.3)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    return fig


def plot_moving_averages(Close_Prices, ma_twenty, ma_Fifty, selected_stocks):

    fig, ax = plt.subplots(
        len(selected_stocks),
        1,
        figsize=(14, 5 * len(selected_stocks)),
        squeeze=False
    )

    for i, stock in enumerate(selected_stocks):

        ax[i, 0].plot(
            Close_Prices[stock],
            label="Actual Price",
            color="blue",
            linewidth=1.2
        )

        ax[i, 0].plot(
            ma_twenty[stock],
            label="20-Day MA",
            color="orange",
            linewidth=1.5
        )

        ax[i, 0].plot(
            ma_Fifty[stock],
            label="50-Day MA",
            color="red",
            linewidth=1.5
        )

        ax[i, 0].set_title(f"{stock} Moving Averages")
        ax[i, 0].set_ylabel("Closing Price (USD)")
        ax[i, 0].legend(frameon=False)
        ax[i, 0].grid(axis="y", alpha=0.3)

        ax[i, 0].spines["top"].set_visible(False)
        ax[i, 0].spines["right"].set_visible(False)

    ax[-1, 0].set_xlabel("Date")

    fig.tight_layout()

    return fig


def plot_returns_distribution(returns, selected_stocks):

    all_returns = returns[selected_stocks].to_numpy().flatten()
    all_returns = all_returns[~np.isnan(all_returns)]

    bins = np.linspace(
        all_returns.min(),
        all_returns.max(),
        51
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    for stock in selected_stocks:

        ax.hist(
            returns[stock].dropna(),
            bins=bins,
            histtype="step",
            linewidth=2,
            color=colors[stock],
            label=stock
        )

    ax.axvline(
        x=0,
        color="black",
        linestyle="--",
        linewidth=1.2,
        alpha=0.6
    )

    ax.set_title("Daily Returns Distribution Comparison", fontsize=16)
    ax.set_xlabel("Daily Returns (%)")
    ax.set_ylabel("Frequency")

    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.3)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    return fig


def plot_trading_volume(volume, selected_stocks):

    fig, ax = plt.subplots(figsize=(12, 6))

    monthly_volume = (
        volume[selected_stocks]
        .resample("ME")
        .mean() / 1e6
    )

    x = np.arange(len(monthly_volume))

    bar_width = 0.8 / len(selected_stocks)

    for i, stock in enumerate(selected_stocks):

        offset = (
            i - (len(selected_stocks) - 1) / 2
        ) * bar_width

        ax.bar(
            x + offset,
            monthly_volume[stock],
            width=bar_width,
            label=stock,
            color=colors[stock],
            alpha=0.9
        )

    tick_positions = np.arange(0, len(x), 6)

    tick_labels = monthly_volume.index.strftime("%b %Y")

    ax.set_xticks(tick_positions)
    ax.set_xticklabels(
        tick_labels[tick_positions],
        rotation=30,
        ha="right"
    )

    ax.set_title("Monthly Average Daily Trading Volume", fontsize=16)
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Daily Volume (Millions of Shares)")

    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    return fig


def plot_cumulative_returns(Cumulative_Returns, selected_stocks):

    fig, ax = plt.subplots(figsize=(12, 6))

    for stock in selected_stocks:

        ax.plot(
            Cumulative_Returns[stock],
            label=stock,
            color=colors[stock],
            linewidth=2.2
        )

        ax.fill_between(
            Cumulative_Returns.index,
            Cumulative_Returns[stock],
            0,
            color=colors[stock],
            alpha=0.08
        )

    ax.axhline(
        y=0,
        color="black",
        linestyle="--",
        linewidth=1,
        alpha=0.5
    )

    ax.set_title(
        "Cumulative Returns Comparison",
        fontsize=17,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Returns (%)")

    ax.legend(frameon=False)
    ax.grid(axis="y", linestyle="--", alpha=0.2)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    return fig


def plot_volatility(Volatility, selected_stocks):

    fig, ax = plt.subplots(figsize=(12, 6))

    for stock in selected_stocks:

        ax.plot(
            Volatility[stock],
            label=stock,
            color=colors[stock],
            linewidth=1.8
        )

        ax.fill_between(
            Volatility.index,
            Volatility[stock],
            0,
            color=colors[stock],
            alpha=0.08
        )

    ax.set_title(
        "20-Day Rolling Volatility Comparison",
        fontsize=17,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility (Standard Deviation of Daily Returns %)")

    ax.legend(frameon=False)
    ax.grid(axis="y", linestyle="--", alpha=0.2)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    return fig
