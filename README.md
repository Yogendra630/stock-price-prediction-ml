📈 Stock Price Prediction using LSTM (Deep Learning)

This project predicts stock prices using Deep Learning (LSTM Neural Networks) built with TensorFlow/Keras.
The model trains on historical stock data and learns patterns to forecast future stock prices.

The project automatically downloads stock data, trains a model, and saves the trained model for future predictions.

🚀 Features

📊 Download real-time historical stock data using yfinance

🧠 Deep Learning model using LSTM (Long Short-Term Memory)

🔄 Data preprocessing with MinMaxScaler

💾 Automatically saves trained model

📉 Time-series forecasting

⚡ Easy to run with a single command

🧰 Technologies Used

Python

TensorFlow / Keras

NumPy

Pandas

Scikit-Learn

Matplotlib

yFinance

Streamlit (for dashboard support)

📁 Project Structure
stock-price-prediction/
│
├── data/
│   └── stock.csv
│
├── model/
│   └── train_model.py
│
├── utils/
│   └── config.py
│
├── saved_model/
│   └── lstm_stock_model.h5
│
├── main.py
├── requirements.txt
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/Yoendra630/stock-price-prediction.git

Move into the project folder:

cd stock-price-prediction

Install dependencies:

pip install -r requirements.txt
▶️ Run the Project

Run the main program:

python main.py

This will:

Download stock data

Train the LSTM model

Save the trained model

🧠 Model Architecture

The project uses LSTM (Long Short-Term Memory) networks which are ideal for time series prediction.

Model Layers:

LSTM (50 neurons)
LSTM (50 neurons)
Dense (1 neuron output)

Loss Function:

Mean Squared Error (MSE)

Optimizer:

Adam
📊 Data Processing Steps

Download stock data

Select Close Price

Normalize values using MinMaxScaler

Create sequences of 60 time steps

Train LSTM model

Save trained model

💾 Output

After training, the model is saved in:

saved_model/lstm_stock_model.h5

This model can later be used for prediction or deployed in a web app.

📈 Future Improvements

Add Streamlit Dashboard

Real-time stock prediction

Model accuracy visualization

Multi-stock prediction

Hyperparameter tuning

Deploy using Docker / Cloud

🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit pull requests.

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Yogendra Maurya
