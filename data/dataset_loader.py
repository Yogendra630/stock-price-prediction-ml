import yfinance as yf
import pandas as pd

def download_stock_data(symbol, start, end):
    print("Downloading stock data...")
    data = yf.download(symbol, start=start, end=end)

    if data.empty:
        raise ValueError("No data found")

    data.reset_index(inplace=True)

    return data


def save_dataset(data, filename="stock_data.csv"):
    data.to_csv(filename, index=False)
    print("Dataset saved:", filename)


def load_dataset(filename="stock.csv"):
    data = pd.read_csv(filename)
    return data