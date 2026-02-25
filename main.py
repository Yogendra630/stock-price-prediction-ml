from data.dataset_loader import download_stock_data
from model.train_model import ModelTrainer
import utils.config as config

def main():

    data = download_stock_data(
        config.STOCK_SYMBOL,
        config.START_DATE,
        config.END_DATE
    )

    trainer = ModelTrainer(data)

    trainer.train()

if __name__ == "__main__":
    main()