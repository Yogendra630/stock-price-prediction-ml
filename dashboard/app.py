import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prediction.predict_future import Predictor

st.title("Stock Price Prediction")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    predictor = Predictor(uploaded_file)

    predictions, data = predictor.predict()

    st.subheader("Predicted Graph")

    fig = plt.figure(figsize=(10,5))

    plt.plot(data.values, label="Actual Price")
    plt.plot(range(60, 60+len(predictions)), predictions, label="Predicted Price")

    plt.legend()

    st.pyplot(fig)