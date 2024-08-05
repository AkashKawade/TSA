from datetime import timedelta
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

class ARIMAForecasting:
    @staticmethod
    def forecast(df, series, order=(2, 1, 2), forecast_steps=1):
        model = ARIMA(series, order=order)
        model_fit = model.fit()

        last_date = df.index[-1]
        prediction_dates = []
        start_date = last_date + timedelta(days=1)

        while len(prediction_dates) < forecast_steps:
            if start_date.weekday() < 5:  # Monday to Friday are considered business days
                prediction_dates.append(start_date)
            start_date += timedelta(days=1)

        forecast = model_fit.forecast(steps=forecast_steps)

        prediction_df = pd.DataFrame({'Date': prediction_dates, 'Predicted_Close': forecast})
        prediction_df.set_index('Date', inplace=True)

        return prediction_df