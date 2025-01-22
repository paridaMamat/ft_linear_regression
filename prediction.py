import json

# Load parameters
with open('theta.json', 'r') as f:
    params = json.load(f)

theta0 = params['theta0']
theta1 = params['theta1']

# Prediction
while True:
    mileage = input("Enter mileage (or 'q' to quit): ")
    if mileage.lower() == 'q':
        break
    try:
        mileage = float(mileage)
        price = theta0 + theta1 * mileage
        print(f"Estimated price: {price}")
    except ValueError:
        print("Please enter a valid number.")
