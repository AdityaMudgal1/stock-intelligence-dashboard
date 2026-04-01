from fastapi import APIRouter
from app.services import (
    get_companies,
    get_stock_data,
    get_summary,
    compare_stocks,
    predict_price,
    correlation
)

router = APIRouter()

@router.get("/companies")
def companies():
    return get_companies()

@router.get("/data/{symbol}")
def stock_data(symbol: str):
    return get_stock_data(symbol)

@router.get("/summary/{symbol}")
def summary(symbol: str):
    return get_summary(symbol)

@router.get("/compare")
def compare(symbol1: str, symbol2: str):
    return compare_stocks(symbol1, symbol2)

# 🔥 NEW ENDPOINT
@router.get("/predict/{symbol}")
def predict(symbol: str):
    return predict_price(symbol)

# 🔥 NEW ENDPOINT
@router.get("/correlation")
def corr(symbol1: str, symbol2: str):
    return correlation(symbol1, symbol2)