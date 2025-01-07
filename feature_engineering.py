import pandas as pd

# Load the cleaned stock data (ensure correct path)
data = pd.read_csv('data/cleaned_stock_data.csv', index_col=0, parse_dates=True)

# Inspect the first few rows and the column types
print(data.head())
print(data.dtypes)

# Convert 'Close' column to numeric, forcing errors to NaN
data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

# Check if there are any NaN values in the 'Close' column
print(f"Missing values in 'Close' column: {data['Close'].isna().sum()}")

# Handle missing values - forward-fill or drop rows
# Option 1: Fill missing values with the previous valid value
data['Close'].fillna(method='ffill', inplace=True)

# Option 2: Alternatively, drop rows with missing values in 'Close'
# data.dropna(subset=['Close'], inplace=True)

# Re-check missing values
print(f"Missing values after cleaning: {data['Close'].isna().sum()}")

# Calculate moving averages and Bollinger Bands
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['Upper_Band'] = data['SMA_50'] + 2 * data['Close'].rolling(window=50).std()
data['Lower_Band'] = data['SMA_50'] - 2 * data['Close'].rolling(window=50).std()

# Save the modified data with features
data.to_csv('data/stock_data_with_features.csv')

print("Feature engineering completed and saved!")
