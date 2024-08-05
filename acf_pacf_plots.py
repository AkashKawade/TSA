import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

class ACF_PACF_Plots:
    @staticmethod
    def plot_acf_pacf(series):
        plot_acf(series)
        plt.show()
        plot_pacf(series)
        plt.show()
