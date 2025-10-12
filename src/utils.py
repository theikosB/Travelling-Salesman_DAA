import pandas as pd

def load_cities(dataset_path: str):
    """
    Load cities from dataset CSV with columns:
    City, X, Y

    Parameters:
        dataset_path (str): Path to dataset (tiny.csv, small.csv, etc.)

    Returns:
        DataFrame with columns: City, X, Y
    """
    # Read CSV with headers or manually name them
    df = pd.read_csv(dataset_path, header=None, names=["City", "X", "Y"])

    # Convert coordinates to numeric
    df["X"] = pd.to_numeric(df["X"], errors="coerce")
    df["Y"] = pd.to_numeric(df["Y"], errors="coerce")

    # Create a copy for pretty printing
    df_print = df.copy()
    df_print["X"] = df_print["X"].round(4)
    df_print["Y"] = df_print["Y"].round(4)

    print("\nLoaded cities from:", dataset_path)
    print(df_print.to_string(index=False))

    return df
