import matplotlib.pyplot as plt

def plot_stock_data(data, ticker, window):
    plt.figure(figsize=(14, 7))
    plt.plot(data['date'], data['close_price'], label='Close Price', color='blue')
    plt.plot(data['date'], data['SMA'], label=f'SMA {window} Days', color='orange')
    plt.title(f'{ticker} Stock Price and {window}-Day SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
