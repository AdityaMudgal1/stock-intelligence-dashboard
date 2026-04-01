from app.utils import fetch_stock_data
import numpy as np
from sklearn.linear_model import LinearRegression

COMPANIES = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]


def get_companies():
    return {"companies": COMPANIES}


# 🔥 FIXED FUNCTION (IMPORTANT)
def get_stock_data(symbol):
    df = fetch_stock_data(symbol)

    # ✅ Convert Date to string (fix serialization)
    if "Date" in df.columns:
        df["Date"] = df["Date"].astype(str)

    # ✅ Replace NaN values with 0
    df = df.fillna(0)

    # ✅ Convert all values to native Python types
    df = df.astype(object)

    return df.tail(30).to_dict(orient="records")


def get_summary(symbol):
    df = fetch_stock_data(symbol)

    return {
        "52_week_high": float(df["High"].max()),
        "52_week_low": float(df["Low"].min()),
        "avg_close": float(df["Close"].mean())
    }


def compare_stocks(symbol1, symbol2):
    df1 = fetch_stock_data(symbol1)
    df2 = fetch_stock_data(symbol2)

    return {
        symbol1: float(df1["Close"].pct_change().sum()),
        symbol2: float(df2["Close"].pct_change().sum())
    }


# 🔥 ML Prediction Feature
def predict_price(symbol):
    df = fetch_stock_data(symbol)

    df = df.reset_index()
    X = np.array(range(len(df))).reshape(-1, 1)
    y = df["Close"].values

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[len(df) + 1]])[0]

    return {"predicted_price": float(prediction)}


# 🔥 Correlation Feature
def correlation(symbol1, symbol2):
    df1 = fetch_stock_data(symbol1)
    df2 = fetch_stock_data(symbol2)

    corr = df1["Close"].corr(df2["Close"])

    return {
        "symbol1": symbol1,
        "symbol2": symbol2,
        "correlation": float(corr)
    }