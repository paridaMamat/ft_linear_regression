import numpy as np
import pandas as pd
import json
import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

# Store theta values for animation
theta_history = []
theta_history.append((theta0, theta1))

# Gradient descent
for i in range(iterations):
    pred = theta0 + theta1 * x
    error = pred - y
    tmp_theta0 = theta0 - (learning_rate * np.sum(error) / m)
    tmp_theta1 = theta1 - (learning_rate * np.sum(error * x) / m)
    theta0, theta1 = tmp_theta0, tmp_theta1

    # Save theta values every 500 iterations for animation
    if i % 500 == 0 or i == iterations - 1:
        theta_history.append((theta0, theta1))

    # Debugging: Print every 1000 iterations
    if i % 1000 == 0:
        cost = np.sum(error ** 2) / (2 * m)
        print(f"Iteration {i}: theta0 = {theta0}, theta1 = {theta1}, cost = {cost}")

# Save the parameters
with open('theta.json', 'w') as f:
    json.dump({'theta0': theta0, 'theta1': theta1}, f)

print(f"Training complete. theta0: {theta0}, theta1: {theta1}")

# Animation setup
fig, ax = plt.subplots()
ax.scatter(x, y, label="Data Points")
line, = ax.plot([], [], color='red', label="Regression Line")
ax.legend()
ax.set_xlabel("Normalized Mileage")
ax.set_ylabel("Price")
ax.set_title("Linear Regression Fit")

# Initialize animation function
def init():
    line.set_data([], [])
    return line,

# Animation update function
def update(frame):
    theta0, theta1 = theta_history[frame]
    line.set_data(x, theta0 + theta1 * x)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(theta_history), init_func=init, blit=True, interval=500)

plt.show()
