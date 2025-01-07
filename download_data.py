import yfinance as yf

# Define the stock symbol and the time period
stock_symbol = 'AAPL'  # You can replace this with any stock ticker (e.g., 'GOOGL', 'AMZN')
start_date = '2010-01-01'
end_date = '2023-01-01'

# Download the stock data
data = yf.download(stock_symbol, start=start_date, end=end_date)

# Check the column names to ensure 'Date' exists
print(data.columns)

# Save the data to a CSV file
data.to_csv('data/stock_data.csv')

print("Stock data downloaded and saved!")
