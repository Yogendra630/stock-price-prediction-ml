import numpy as np
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import utils.config as config


class Predictor:

    def __init__(self, file):
        self.file = file

    def predict(self):

        # Load CSV
        df = pd.read_csv(self.file)

        # Ensure Close column exists
        if "Close" not in df.columns:
            raise ValueError("CSV must contain 'Close' column")

        data = df[['Close']]

        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data)

        X_test = []

        for i in range(60, len(scaled_data)):
            X_test.append(scaled_data[i-60:i, 0])

        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

        # Load trained model
        model = load_model(config.MODEL_PATH)

        predictions = model.predict(X_test)
        predictions = scaler.inverse_transform(predictions)

        return predictions, data