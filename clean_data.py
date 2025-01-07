import pandas as pd
data = pd.read_csv('data/stock_data.csv', index_col=0, parse_dates=True)
print(data.head())

# Clean the data (handling missing values, etc.)
data.fillna(method='ffill', inplace=True)  # Forward fill missing data

# Save cleaned data to a new CSV file
data.to_csv('data/cleaned_stock_data.csv')

print("Data cleaned and saved!")
