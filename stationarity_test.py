from statsmodels.tsa.stattools import adfuller

class StationarityTest:
    @staticmethod
    def adfuller_test(series):
        result = adfuller(series)
        labels = ["ADF test statistics", "p-value", "lags used", "Number of observations"]
        for value, label in zip(result, labels):
            print(f"{label}: {value}")
        if result[1] <= 0.05:
            print('Series is Stationary')
        else:
            print('Series is Not Stationary')
