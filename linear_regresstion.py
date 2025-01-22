import numpy as np
import pandas as pd
import json
import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data.csv')
x = df.iloc[:, 0].values
y = df.iloc[:, 1].values

# Normalize the input data (min-max scaling)
x = (x - np.min(x)) / (np.max(x) - np.min(x))

# Initialize parameters
theta0 = 0
theta1 = 0
learning_rate = 0.01  # Reduced learning rate
iterations = 10000  # Increased iterations
m = len(x)

# Gradient descent
for _ in range(iterations):
    pred = theta0 + theta1 * x
    error = pred - y
    tmp_theta0 = theta0 - (learning_rate * np.sum(error) / m)
    tmp_theta1 = theta1 - (learning_rate * np.sum(error * x) / m)
    theta0, theta1 = tmp_theta0, tmp_theta1

    # Debugging: Print every 1000 iterations
    if _ % 1000 == 0:
        cost = np.sum(error ** 2) / (2 * m)
        print(f"Iteration {_}: theta0 = {theta0}, theta1 = {theta1}, cost = {cost}")

# Save the parameters
with open('theta.json', 'w') as f:
    json.dump({'theta0': theta0, 'theta1': theta1}, f)

print(f"Training complete. theta0: {theta0}, theta1: {theta1}")

# Plot data and regression line
plt.scatter(x, y, label="Data Points")
plt.plot(x, theta0 + theta1 * x, color='red', label="Regression Line")
plt.legend()
plt.xlabel("Normalized Mileage")
plt.ylabel("Price")
plt.title("Linear Regression Fit")
plt.show()