class Differencing:
    @staticmethod
    def difference(series):
        return series - series.shift(1)
