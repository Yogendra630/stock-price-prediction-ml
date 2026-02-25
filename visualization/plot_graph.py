import matplotlib.pyplot as plt


class Visualizer:

    def plot_prices(self, actual, predicted):

        plt.figure(figsize=(12,6))

        plt.plot(actual,
                 color="blue",
                 label="Actual Price")

        plt.plot(predicted,
                 color="red",
                 label="Predicted Price")

        plt.title("Stock Price Prediction")

        plt.xlabel("Time")

        plt.ylabel("Stock Price")

        plt.legend()

        plt.show()