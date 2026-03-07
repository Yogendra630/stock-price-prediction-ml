<h1 align="center">🚀 Stock Price Prediction using LSTM</h1>

<p align="center">
<b>Deep Learning | Time Series Forecasting | Artificial Intelligence</b>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.9-blue?logo=python">
<img src="https://img.shields.io/badge/TensorFlow-DeepLearning-orange?logo=tensorflow">
<img src="https://img.shields.io/badge/AI-LSTM-green">
<img src="https://img.shields.io/badge/Status-Active-success">
<img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project builds a <b>Stock Price Prediction System</b> using 
<b>Deep Learning with LSTM (Long Short-Term Memory)</b> networks.
</p>

<p>
The system automatically downloads historical stock market data, 
processes it, trains a deep learning model, and saves the trained model 
for future predictions.
</p>

<ul>
<li>📊 Automatic stock data collection</li>
<li>🧠 Deep Learning LSTM model</li>
<li>📉 Time series forecasting</li>
<li>💾 Model saving for predictions</li>
</ul>

<hr>

<h2>🧠 Model Architecture</h2>

<pre>
Input Data (60 Time Steps)
        ↓
LSTM Layer (50 Units)
        ↓
LSTM Layer (50 Units)
        ↓
Dense Layer
        ↓
Predicted Stock Price
</pre>

<table border="1" cellpadding="8">
<tr>
<th>Parameter</th>
<th>Value</th>
</tr>

<tr>
<td>Optimizer</td>
<td>Adam</td>
</tr>

<tr>
<td>Loss Function</td>
<td>Mean Squared Error</td>
</tr>

<tr>
<td>Epochs</td>
<td>5</td>
</tr>

<tr>
<td>Batch Size</td>
<td>32</td>
</tr>

</table>

<hr>

<h2>🛠 Technologies Used</h2>

<ul>
<li>🐍 Python</li>
<li>🤖 TensorFlow / Keras</li>
<li>📊 Pandas</li>
<li>🔢 NumPy</li>
<li>📉 Scikit-Learn</li>
<li>📡 yFinance API</li>
<li>📈 Matplotlib</li>
<li>🌐 Streamlit</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
stock-price-prediction
│
├── data
│   └── stock.csv
│
├── model
│   └── train_model.py
│
├── utils
│   └── config.py
│
├── saved_model
│   └── lstm_stock_model.h5
│
├── main.py
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>⚙️ Installation</h2>

<h3>1️⃣ Clone Repository</h3>

<pre>
git clone https://github.com/yourusername/stock-price-prediction.git
</pre>

<h3>2️⃣ Open Project Folder</h3>

<pre>
cd stock-price-prediction
</pre>

<h3>3️⃣ Install Libraries</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>▶️ Run the Project</h2>

<pre>
python main.py
</pre>

<p>The program will automatically:</p>

<ul>
<li>Download stock data</li>
<li>Preprocess the dataset</li>
<li>Train the LSTM model</li>
<li>Save the trained model</li>
</ul>

<hr>

<h2>📊 Data Processing Pipeline</h2>

<pre>
Stock Data Download
        ↓
Select Closing Price
        ↓
Data Normalization
        ↓
Create Time Series Sequences
        ↓
Train LSTM Model
        ↓
Save Model
</pre>

<hr>

<h2>💾 Model Output</h2>

<p>The trained model will be saved in:</p>

<pre>
saved_model/lstm_stock_model.h5
</pre>

<p>
This model can be used later for:
</p>

<ul>
<li>📊 Stock prediction</li>
<li>🌐 Web applications</li>
<li>📈 Real-time forecasting</li>
</ul>

<hr>

<h2>📈 Example Prediction Graph</h2>

<p align="center">
<img src="stock.png" width="600">
</p>

<hr>

<h2>🔮 Future Improvements</h2>

<ul>
<li>✨ Interactive Streamlit dashboard</li>
<li>📡 Real-time stock prediction</li>
<li>📊 Model accuracy visualization</li>
<li>☁️ Cloud deployment</li>
<li>📱 Web application interface</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>

<p>
Contributions are welcome!  
Feel free to fork the repository and submit pull requests.
</p>

<hr>

<h2>📜 License</h2>

<p>
This project is licensed under the <b>MIT License</b>.
</p>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Yogendra Maurya</b><br>

</p>

<hr>

<p align="center">
⭐ If you like this project, please give it a star on GitHub!
</p>
