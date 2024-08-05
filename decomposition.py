import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

class Decomposition:
    @staticmethod
    def decompose(series, model='multiplicative', period=7):
        decomposition = seasonal_decompose(series, model=model, period=period)
        fig = decomposition.plot()
        fig.set_size_inches(15, 8)
        plt.show()
