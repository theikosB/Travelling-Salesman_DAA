import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from utils import load_cities


def euclidean_distance(x1, y1, x2, y2):
    """Compute Euclidean distance between 2 points."""
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def tsp_nearest_neighbor(cities, start_index=0):
    """
    Nearest Neighbor TSP heuristic.

    Parameters:
        cities (DataFrame): City, X, Y
        start_index (int): Index of starting city

    Returns:
        (tour, total_length)
    """
    n = len(cities)
    visited = [False] * n
    tour = [start_index]
    visited[start_index] = True
    total_length = 0

    current = start_index
    for _ in range(n - 1):
        nearest, min_dist = None, float("inf")
        for j in range(n):
            if not visited[j]:
                d = euclidean_distance(
                    cities.loc[current, "X"], cities.loc[current, "Y"],
                    cities.loc[j, "X"], cities.loc[j, "Y"]
                )
                if d < min_dist:
                    nearest, min_dist = j, d
        tour.append(nearest)
        visited[nearest] = True
        total_length += min_dist
        current = nearest

    # return to start
    total_length += euclidean_distance(
        cities.loc[current, "X"], cities.loc[current, "Y"],
        cities.loc[start_index, "X"], cities.loc[start_index, "Y"]
    )
    tour.append(start_index)

    return tour, total_length


def tsp_nearest_fragment(cities):
    """
    Multi-start Nearest Neighbor (Nearest Fragment).
    Runs NN from every city and picks the best tour.
    
    Parameters:
        cities (DataFrame): City, X, Y
    
    Returns:
        (best_tour, best_length)
    """
    best_length = float("inf")
    best_tour = None

    for start in range(len(cities)):
        tour, total_length = tsp_nearest_neighbor(cities, start_index=start)
        if total_length < best_length:
            best_length = total_length
            best_tour = tour

    return best_tour, best_length


import matplotlib.pyplot as plt
import networkx as nx

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
