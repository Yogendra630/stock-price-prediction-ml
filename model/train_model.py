import numpy as np
import pandas as pd
from preprocessing.data_preprocessing import DataPreprocessor
from model.lstm_model import LSTMModel
import utils.config as config


class ModelTrainer:

    def __init__(self, dataframe):
        self.data = dataframe
        self.processor = DataPreprocessor()

    def prepare_data(self):

        close_prices = self.data['Close'].values.reshape(-1,1)

        scaled = self.processor.scale_data(close_prices)

        x, y = self.processor.create_sequences(
            scaled,
            config.TIME_STEP
        )

        return x, y

    def train(self):

        x, y = self.prepare_data()

        print("Training samples:", x.shape)

        model_builder = LSTMModel()

        model = model_builder.build_model(
            (x.shape[1], 1)
        )

        model.fit(
            x,
            y,
            epochs=config.EPOCHS,
            batch_size=config.BATCH_SIZE
        )

        model.save(config.MODEL_PATH)

        print("Model saved")

        return model