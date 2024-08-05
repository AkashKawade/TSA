from data_loader import DataLoader
from stationarity_test import StationarityTest
from differencing import Differencing
from acf_pacf_plots import ACF_PACF_Plots
from decomposition import Decomposition
from arima_forecasting import ARIMAForecasting
import matplotlib.pyplot as plt

# Load data
data_loader = DataLoader('NIFTY 50 05.csv')
df = data_loader.load_data()

# Plot close prices
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['Close'])
plt.title('Historical Close Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.show()

# Stationarity Test
StationarityTest.adfuller_test(df['Close'])

# Differencing
df['Close_diff'] = Differencing.difference(df['Close'])
StationarityTest.adfuller_test(df['Close_diff'].dropna())

df['Close_diff'].plot()
plt.show()

# ACF and PACF Plots
ACF_PACF_Plots.plot_acf_pacf(df['Close_diff'].dropna())

# Decomposition
Decomposition.decompose(df['Close'])

# ARIMA Model and Forecast
prediction_df = ARIMAForecasting.forecast(df, df['Close'])
print(prediction_df)
