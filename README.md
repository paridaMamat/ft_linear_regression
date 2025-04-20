# Linear Regression Price Predictor

This project implements a simple **linear regression model** to estimate the price of a car based on its mileage. It consists of two main components:

- A **training script** (`linear_regresstion.py`) that reads a dataset, performs gradient descent to learn model parameters, and optionally displays an animated visualization of the training process.
- A **prediction script** (`prediction.py`) that loads the learned model and allows users to enter mileage values to get predicted prices.

---

##  Project Structure

- `linear_regresstion.py`: Trains the linear regression model using gradient descent on mileage vs price data, normalizes inputs, and saves the learned parameters.
- `prediction.py`: Loads the saved parameters and allows real-time price prediction via command-line input.
- `theta.json`: Output file containing the trained model parameters (`theta0`, `theta1`) and mileage normalization bounds.
- `data.csv`: The dataset containing car mileage and corresponding prices (assumed to have two columns: mileage and price).

---

##  Dependencies

Make sure the following Python packages are installed:

```bash

pip install numpy pandas matplotlib
