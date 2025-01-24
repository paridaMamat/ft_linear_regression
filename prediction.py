import json


def load_parameters(filename):
    """Load parameters from a JSON file."""
    try:
        with open(filename, 'r') as f:
            params = json.load(f)

        # Ensure required keys are present in the JSON file
        required_keys = ['theta0', 'theta1', 'min_mileage', 'max_mileage']
        if not all(key in params for key in required_keys):
            raise KeyError(f"JSON file is missing one or more required keys: {required_keys}")

        return params['theta0'], params['theta1'], params['min_mileage'], params['max_mileage']
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please make sure it exists.")
        return None, None, None, None
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON. Please check its contents.")
        return None, None, None, None
    except KeyError as e:
        print(f"Error: {e}")
        return None, None, None, None
    except Exception as e:
        print(f"Unexpected error while loading parameters: {e}")
        return None, None, None, None


def predict_price(theta0, theta1, min_mileage, max_mileage):
    """Run a prediction loop for mileage input."""
    while True:
        mileage = input("Enter mileage (or 'q' to quit): ")
        if mileage.lower() in ['q', 'quit']:
            break
        try:
            mileage = float(mileage)
            if mileage < 0:
                print("Please enter a positive number.")
                continue
            if not (min_mileage <= mileage <= max_mileage):
                print(f"Please enter a mileage between {min_mileage} and {max_mileage}.")
                continue
            price = theta0 + theta1 * mileage
            print(f"Estimated price: {price}")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")
    print('Goodbye!')


def main():
    """Main function to load parameters and start prediction."""
    # Load parameters from JSON file
    theta0, theta1, min_mileage, max_mileage = load_parameters('theta.json')

    # If parameters couldn't be loaded, exit the program
    if theta0 is None or theta1 is None or min_mileage is None or max_mileage is None:
        print("Failed to load parameters. Exiting...")
        return

    print("Parameters loaded successfully!")
    print(f"Intercept (theta0): {theta0}, Slope (theta1): {theta1}")
    print(f"Valid mileage range: {min_mileage} - {max_mileage}")

    # Start the prediction loop
    predict_price(theta0, theta1, min_mileage, max_mileage)


if __name__ == "__main__":
    main()
