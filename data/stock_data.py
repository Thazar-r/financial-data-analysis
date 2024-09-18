import requests
import pandas as pd
from sqlalchemy.orm import sessionmaker
from models.database import StockPrice, Session

def fetch_stock_data(ticker, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}&outputsize=full'
    response = requests.get(url)
    data = response.json()
    
    prices = data.get('Time Series (Daily)', {})
    stock_data = []
    
    for date, metrics in prices.items():
        stock_data.append({
            'ticker': ticker,
            'date': pd.to_datetime(date),
            'open_price': float(metrics['1. open']),
            'high_price': float(metrics['2. high']),
            'low_price': float(metrics['3. low']),
            'close_price': float(metrics['4. close']),
            'volume': int(metrics['5. volume'])
        })
    
    return stock_data

def insert_stock_data(stock_data):
    session = Session()
    for entry in stock_data:
        stock_price = StockPrice(**entry)
        session.add(stock_price)
    session.commit()
    session.close()
