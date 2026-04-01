# Stock Intelligence Dashboard

## About the Project

This project is a simple stock data dashboard where I worked on fetching, analyzing, and visualizing stock market data.

The goal was to build a small system that can:
- Fetch real stock data  
- Process and analyze it  
- Provide useful insights through APIs  

---

## Features

- Fetches stock data using yfinance  
- Cleans missing values and formats data  
- Calculates:
  - Daily Return  
  - 7-day Moving Average  
  - 52-week High & Low  
- Added a custom volatility metric  

---

## API Endpoints

- /companies → List of stocks  
- /data/{symbol} → Last 30 days data  
- /summary/{symbol} → 52-week stats  
- /compare → Compare two stocks  
- /predict/{symbol} → Price prediction (ML)  
- /correlation → Relationship between stocks  

Swagger Docs:  
http://127.0.0.1:8000/docs  

---

## Extra Work Done

To go beyond the basics, I added:
- A simple ML model for price prediction  
- Correlation analysis between stocks  
- Volatility calculation  

---

## How to Run

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
uvicorn app.main:app --reload  

---

## What I Learned

- Handling real-world data (NaN values, formats, etc.)  
- Working with FastAPI to build APIs  
- Debugging issues like serialization and data structure problems  
- Basic use of ML for predictions  

---

## Author

Aditya Mudgal