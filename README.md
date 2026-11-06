# Financial Data Analysis Dashboard 📊

My first step towards my Machine Learning journey!

This project is a simple financial data analysis dashboard built to strengthen my understanding of data handling, data analysis, and data visualisation using Python.

I analysed historical stock-market data from three major technology companies: **Apple (AAPL), Google (GOOG), and Microsoft (MSFT)**.

The goal was to explore how these companies performed over time and learn how to turn raw financial data into meaningful visual insights.

## 🎯 Project Objectives

- Learn how to retrieve real-world financial data.
- Practise data handling and manipulation using Pandas.
- Understand stock returns, moving averages, and volatility.
- Create meaningful visualisations using Matplotlib.
- Build a simple web-based dashboard using Streamlit.
- Learn the basics of Git and GitHub for version control.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **yfinance** – Downloading historical stock-market data.
- **Pandas** – Data manipulation, cleaning, and analysis.
- **NumPy** – Numerical operations and calculations.
- **Matplotlib** – Creating charts and visualisations.
- **Streamlit** – Building the dashboard interface.
- **Git & GitHub** – Version control and project hosting.

## 📈 Features and Analysis

The dashboard includes the following visualisations and analysis:

1. **Historical Closing Prices** – Compares the closing prices of all three companies.
2. **Moving Averages** – Displays 20-day and 50-day moving averages to understand price trends.
3. **Daily Returns Distribution** – Examines the distribution of daily stock returns.
4. **Trading Volume** – Compares monthly average daily trading volume.
5. **Cumulative Returns** – Tracks the growth of stock prices over the selected period.
6. **Rolling Volatility** – Examines changes in stock price volatility using a 20-day rolling standard deviation.
7. **Performance Summary** – Displays cumulative returns, average daily returns, and daily volatility.
8. **Key Findings** – Highlights comparisons such as the highest cumulative return and lowest daily volatility.

## 📅 Dataset

- **Data Source:** Yahoo Finance
- **Library:** yfinance
- **Companies:** Apple, Google, Microsoft
- **Start Date:** January 2020
- **End Date:** December 2025
- **Interval:** Daily

The data was downloaded directly using the yfinance library. I used Pandas to inspect, manipulate, and prepare the dataset for analysis. The initial dataset did not contain missing values in the selected fields.

## 📚 What I Learned

This project was primarily a learning experience.

- Worked with real-world financial datasets instead of only practice datasets.
- Improved my understanding of Pandas DataFrames, indexing, selecting columns, and handling time-series data.
- Practised calculating daily returns, cumulative returns, moving averages, and rolling volatility.
- Used Matplotlib to experiment with different chart types and visualisation styles.
- Learned how Streamlit can turn Python scripts into web-based dashboards.
- Explored Streamlit caching using `@st.cache_data` to avoid repeatedly downloading the same dataset.
- Learned how to organise a project into separate Python modules.
- Practised Git commands, commits, and uploading a project to GitHub.

I used ChatGPT as a learning assistant while working with Streamlit, since it was relatively new to me. I experimented with the code, made changes, and learned how the different parts of the dashboard work.

I also used NumPy to a limited extent in this project. I plan to strengthen my understanding of it through further projects.

## 🚀 How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/sehdi-giidii/Financial_Data_Analysis_Dashboard.git
```

**2. Navigate to the project directory**

```bash
cd Financial_Data_Analysis_Dashboard
```

**3. Create a virtual environment (optional but recommended)**

```bash
python -m venv .venv
```

**4. Activate the virtual environment (Windows)**

```bash
.venv\Scripts\activate
```

**5. Install the required libraries**

```bash
pip install -r requirements.txt
```

**6. Run the Streamlit application**

```bash
python -m streamlit run app.py
```

The dashboard will open in your browser.

## ⚠️ Disclaimer

This project is intended for educational and analytical purposes only. Historical stock performance does not guarantee future results. The analysis is based on historical closing prices and does not represent investment advice or total returns including dividends.

## 🔮 Future Improvements

- Improve my understanding and use of NumPy.
- Explore more advanced financial data analysis techniques.
- Improve the dashboard layout and visual presentation.
- Add more companies and extend the analysis.
- Continue developing my data analysis skills as I progress towards Machine Learning.

---

**This is just the beginning of my Machine Learning journey. More projects and improvements to come!** 🚀