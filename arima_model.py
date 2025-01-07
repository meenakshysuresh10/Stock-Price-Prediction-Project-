import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt




data = pd.read_csv('data/stock_data_with_features.csv')
print(data.head())
print(data.columns)

train_data = data['Close']


model = ARIMA(train_data, order=(5, 1, 0))
model_fit = model.fit()

# Make a prediction
forecast = model_fit.forecast(steps=30)  # Predict next 30 days

# Plot the prediction
plt.plot(train_data, label='Historical Data')
plt.plot(forecast, label='Predicted', color='red')
plt.legend()
plt.show()

# Save the model
model_fit.save('models/arima_model.pkl')

print("ARIMA model trained and forecasted!")
