import numpy as np
import pandas as pd
import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


matplotlib.use('TkAgg')  # Use the TkAgg backend


# Gradient Descent Function
def gradient_descent(theta0, theta1, x, y, learning_rate, iterations, m):
    theta_history = [(theta0, theta1)]
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

    return theta0, theta1, theta_history


# Function to create and display the animation
def animate_regression(x_original, y, theta_history, x_min, x_max):
    fig, ax = plt.subplots()
    ax.scatter(x_original, y, label="Data Points")
    line, = ax.plot([], [], color='red', label="Regression Line")
    ax.legend()
    ax.set_xlabel("Mileage")
    ax.set_ylabel("Price")
    ax.set_title("Linear Regression Fit (Original Scale)")

    # Set y-axis to start from 0 with custom scaling
    max_y = max(y)
    margin = 500  # Optional margin above the maximum value
    ax.set_ylim(0, max_y + margin)

    # Customize y-axis ticks
    custom_ticks = list(range(0, 4001, 500)) + list(range(5000, int(max_y) + margin + 1000, 1000))
    ax.set_yticks(custom_ticks)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        # Ensure frame stops at the last value
        if frame >= len(theta_history) - 1:
            frame = len(theta_history) - 1

        # Extract the corresponding parameters for the frame
        theta0, theta1 = theta_history[frame]

        # Unnormalize parameters for the frame
        frame_theta1 = theta1 / (x_max - x_min)
        frame_theta0 = theta0 - (frame_theta1 * x_min)

        # Update the regression line
        line.set_data(x_original, frame_theta0 + frame_theta1 * x_original)
        return line,

    ani = FuncAnimation(
        fig,
        update,
        frames=len(theta_history),
        init_func=init,
        blit=True,
        interval=500,
        repeat=False
    )

    plt.show()


# Main Function to Handle the Entire Process
def main():
    try:
        # Load the dataset
        try:
            df = pd.read_csv('data.csv')
            x_original = df.iloc[:, 0].values  # Real mileage
            y = df.iloc[:, 1].values

            if len(x_original) != len(y) or len(x_original) == 0:
                raise ValueError("Dataset is empty or columns do not match in length.")
        except FileNotFoundError:
            raise FileNotFoundError("The file 'data.csv' was not found. Please check the path.")
        except pd.errors.EmptyDataError:
            raise ValueError("The dataset is empty. Please provide a valid dataset.")

        # Normalize the input data (min-max scaling)
        x_min = np.min(x_original)
        x_max = np.max(x_original)
        if x_max == x_min:
            raise ValueError("All mileage values are the same. Cannot perform normalization.")
        x = (x_original - x_min) / (x_max - x_min)

        # Initialize parameters
        theta0 = 0
        theta1 = 0
        learning_rate = 0.01  # Reduced learning rate
        iterations = 10000  # Increased iterations
        m = len(x)

        # Gradient descent
        theta0, theta1, theta_history = gradient_descent(theta0, theta1, x, y, learning_rate, iterations, m)

        # Unnormalize parameters
        unnormalized_theta1 = theta1 / (x_max - x_min)
        unnormalized_theta0 = theta0 - (unnormalized_theta1 * x_min)
        x_min = float(x_min)
        x_max = float(x_max)

        # Save the parameters
        with open('theta.json', 'w') as f:
            json.dump({'theta0': unnormalized_theta0, 'theta1': unnormalized_theta1, 'min_mileage': x_min, 'max_mileage': x_max}, f)

        print(f"Training complete. Intercept (theta0): {unnormalized_theta0}, Slope (theta1): {unnormalized_theta1}")

        # Animate the regression
        animate_regression(x_original, y, theta_history, x_min, x_max)

    except Exception as e:
        print(f"An error occurred: {e}")


# Entry Point
if __name__ == "__main__":
    main()
