import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol: str):
    df = yf.download(symbol, period="1y", interval="1d")

    # ✅ FIX 1: Handle multi-index columns (CRITICAL FIX)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    # ✅ Clean data
    df.dropna(inplace=True)

    # ✅ Metrics
    df["Daily Return"] = (df["Close"] - df["Open"]) / df["Open"]
    df["7D MA"] = df["Close"].rolling(window=7).mean()
    df["52W High"] = df["High"].rolling(window=252).max()
    df["52W Low"] = df["Low"].rolling(window=252).min()

    # 🔥 Custom metric
    df["Volatility"] = df["Close"].pct_change().rolling(7).std()

    return df