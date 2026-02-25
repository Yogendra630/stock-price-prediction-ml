import numpy as np
from sklearn.preprocessing import MinMaxScaler


class DataPreprocessor:

    def __init__(self):
        self.scaler = MinMaxScaler(feature_range=(0,1))

    def scale_data(self, data):
        scaled = self.scaler.fit_transform(data)
        return scaled

    def create_sequences(self, data, time_step=60):
        x = []
        y = []

        for i in range(time_step, len(data)):
            x.append(data[i-time_step:i])
            y.append(data[i])

        return np.array(x), np.array(y)

    def inverse_transform(self, data):
        return self.scaler.inverse_transform(data)