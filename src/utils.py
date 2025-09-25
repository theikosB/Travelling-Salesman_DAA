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

    # Assume first column contains city/location names
    city_names = df.iloc[:, 0].dropna().unique()

    # Pick N cities
    if n_cities > len(city_names):
        raise ValueError(f"Requested {n_cities} cities, but dataset only has {len(city_names)}")

    np.random.seed(seed)
    chosen_cities = np.random.choice(city_names, size=n_cities, replace=False)

    # Generate synthetic random coordinates (range 0–100)
    coords = np.random.randint(0, 100, size=(n_cities, 2))

    # Combine into DataFrame
    city_df = pd.DataFrame({
        "City": chosen_cities,
        "X": coords[:, 0],
        "Y": coords[:, 1]
    })

    # Print table
    print("\nSelected Cities with Coordinates:\n")
    print(city_df.to_string(index=False))

    return city_df
