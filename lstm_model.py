import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Load the data
data = pd.read_csv('data/stock_data_with_features.csv')

# Print the column names
print(data.columns)

# Check if data loaded correctly
print(data.head())

# Handle missing values
data = data.fillna(method='ffill')  # Forward fill missing values

# Use 'Close' prices for prediction
data_close = data['Close'].values.reshape(-1, 1)

# Scale the data
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data_close)

# Prepare the data for LSTM model
X, y = [], []
for i in range(60, len(data_scaled)):
    X.append(data_scaled[i-60:i, 0])  # Previous 60 days
    y.append(data_scaled[i, 0])  # Next day's price

X, y = np.array(X), np.array(y)
X = X.reshape((X.shape[0], X.shape[1], 1))  # Reshape for LSTM

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=10, batch_size=32)

# Make predictions
predictions = model.predict(X)

# Reverse the scaling
predictions = scaler.inverse_transform(predictions)

# Plot the predictions
plt.plot(data['Close'], label='Actual Stock Price')
plt.plot(predictions, label='Predicted Stock Price', color='red')
plt.legend()
plt.show()

# Save the LSTM model
model.save('models/lstm_model.h5')

print("LSTM model trained and predictions made!")
