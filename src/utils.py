import pandas as pd
import numpy as np

def load_cities(filename, n_cities=5, seed=42):
    """
    Load dataset and assign random (x, y) coordinates to N cities.

    Parameters:
        filename (str): Path to CSV dataset.
        n_cities (int): Number of cities to select.
        seed (int): Random seed for reproducibility.

    Returns:
        pd.DataFrame: DataFrame with City and (x, y) coordinates.
    """
    # Load dataset
    df = pd.read_csv(filename)

    # Assume first column contains location names
    # dropping empty cells and taking unique values in account
    city_names = df.iloc[:, 0].dropna().unique()
 
    # Ask user until valid input
    # ValueError or StackOverFlowError
    max_cities = len(city_names)
    while True:
        try:
            n_cities = int(input(f"Enter number of cities to use (1–{max_cities}): "))
            if 1 <= n_cities <= max_cities:
                break
            else:
                print(f"Please enter a number between 1 and {max_cities}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # For easy reproducibility
    np.random.seed(seed)
    chosen_cities = np.random.choice(city_names, size=n_cities, replace=False)

    # Generate synthetic random coordinates having range {0–100}x{0-100}
    coords = np.random.randint(0, 100, size=(n_cities, 2))

    # Combine into DataFrame
    city_df = pd.DataFrame({
        "City": chosen_cities,
        "X": coords[:, 0],
        "Y": coords[:, 1]
    })

    # Print table for clarity
    print("\nSelected Cities with Coordinates:\n")
    print(city_df.to_string(index=False))

    return city_df
