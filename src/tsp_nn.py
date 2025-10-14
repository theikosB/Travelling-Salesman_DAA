import numpy as np
from utils import euclidean_distance


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
    for i in range(n - 1):
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

