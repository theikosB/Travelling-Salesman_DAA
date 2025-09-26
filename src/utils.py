import pandas as pd

def load_cities(dataset_path: str):
    """
    Load cities from dataset CSV.
    
    Parameters:
        dataset_path (str): Path to dataset (tiny.csv, small.csv, etc.)

    Returns:
        DataFrame with columns: City, X, Y
    """
    # Read CSV with no headers, just X and Y per row
    df = pd.read_csv(dataset_path, header=None, names=["X", "Y"])

    # Force numeric conversion (safeguard against string values)
    df["X"] = pd.to_numeric(df["X"], errors="coerce")
    df["Y"] = pd.to_numeric(df["Y"], errors="coerce")

    # Add a City column as simple numbering
    df.insert(0, "City", [f"City {i}" for i in range(len(df))])

    # Make a pretty version of the table for printing
    df_print = df.copy()
    df_print["X"] = df_print["X"].round(4)
    df_print["Y"] = df_print["Y"].round(4)

    print("\nLoaded cities from:", dataset_path)
    print(df_print.to_string(index=False))

    return df
