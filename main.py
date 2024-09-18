from data.stock_data import fetch_stock_data, insert_stock_data
from analysis.analysis import calculate_sma
from visualizations.plots import plot_stock_data

def main():
    api_key = 'IJSAZWNGBKF1DBOY'
    ticker = input("Enter the stock ticker: ")
    window = int(input("Enter the moving average window (days): "))
    
    stock_data = fetch_stock_data(ticker, api_key)
    insert_stock_data(stock_data)
    
    data = calculate_sma(ticker, window)
    plot_stock_data(data, ticker, window)

if __name__ == "__main__":
    main()
