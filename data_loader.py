import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def load_data(self):
        df = pd.read_csv(self.filepath)
        df['Date'] = pd.to_datetime(df['Date'])
        df.sort_values('Date', inplace=True)
        df.set_index('Date', inplace=True)
        return df
