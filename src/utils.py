import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

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

    '''
    # Create a copy for pretty printing
    df_print = df.copy()
    df_print["X"] = df_print["X"].round(4)
    df_print["Y"] = df_print["Y"].round(4)

    print("\nLoaded cities from:", dataset_path)
    print(df_print.to_string(index=False))
    '''

    return df


def euclidean_distance(x1, y1, x2, y2):
    """Compute Euclidean distance between 2 points."""
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def calculate_total_distance(cities, tour):
    """Compute total distance of a given tour."""
    total = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities.loc[tour[i], "X"], cities.loc[tour[i], "Y"]
        x2, y2 = cities.loc[tour[i + 1], "X"], cities.loc[tour[i + 1], "Y"]
        total += euclidean_distance(x1, y1, x2, y2)
    return total


def plot_tour(cities, tour, total_length=None, title="TSP Tour"):
    """Plot TSP tour using NetworkX + Matplotlib and overlay tour details."""
    G = nx.Graph()

    # Add nodes
    for i, row in cities.iterrows():
        G.add_node(i, pos=(row["X"], row["Y"]), label=row["City"])

    # Add edges from tour
    edges = [(tour[i], tour[i + 1]) for i in range(len(tour) - 1)]
    G.add_edges_from(edges)

    pos = nx.get_node_attributes(G, "pos")
    labels = nx.get_node_attributes(G, "label")

    plt.figure(figsize=(7, 7))
    nx.draw(
        G, pos, with_labels=True, labels=labels,
        node_color="lightblue", node_size=600,
        font_size=8, font_weight="bold", edge_color="gray"
    )
    plt.title(title)

    # Add tour info text to the bottom-left corner of the plot
    if total_length is not None:
        text_info = f"Tour: {tour}\nTotal Length: {round(total_length, 2)}"
        plt.gcf().text(
            0.02, 0.02, text_info,
            fontsize=8,
            va='bottom', ha='left',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='black')
        )

    plt.show()

