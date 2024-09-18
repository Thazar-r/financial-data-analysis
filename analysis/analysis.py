import pandas as pd
from sqlalchemy.orm import sessionmaker
from models.database import StockPrice, Session

def calculate_sma(ticker, window):
    session = Session()
    df = pd.read_sql(session.query(StockPrice).filter_by(ticker=ticker).statement, session.bind)
    session.close()
    
    df['SMA'] = df['close_price'].rolling(window=window).mean()
    return df[['date', 'close_price', 'SMA']]
