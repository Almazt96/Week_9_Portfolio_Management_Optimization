# Task 1: Data Sourcing, Preprocessing, and Pipeline Engineering
import pandas as pd
import numpy as np
import yfinance as yf
def download_and_clean_data(tickers, start_date, end_date):
    print(f"Extracting historical data for: {tickers}")
    raw_data = yf.download(tickers, start=start_date, end=end_date)["Close"]
    # Handle missing values robustly
    cleaned_data = raw_data.ffill().bfill()
    # Calculate simple and log returns
    daily_returns = cleaned_data.pct_change().dropna()
    log_returns = np.log(cleaned_data / cleaned_data.shift(1)).dropna()

    # Calculate cumulative returns
    cumulative_returns = (1 + daily_returns).cumprod() - 1
    return cleaned_data, daily_returns, log_returns, cumulative_returns
if __name__ == "__main__":
    assets = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    prices, returns, log_ret, cum_ret = download_and_clean_data(assets, "2023-01-01",
    "2026-06-30")
    print("Data pipeline executed successfully. Dimensions:", returns.shape)