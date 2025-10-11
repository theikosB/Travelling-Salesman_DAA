import numpy as np
from tsp_nn import euclidean_distance

def calculate_total_distance(cities, tour):
    """Compute total distance of a given tour."""
    total = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities.loc[tour[i], "X"], cities.loc[tour[i], "Y"]
        x2, y2 = cities.loc[tour[i + 1], "X"], cities.loc[tour[i + 1], "Y"]
        total += euclidean_distance(x1, y1, x2, y2)
    return total


def tsp_2opt(cities, tour):
    """
    Pairwise Exchange for TSP.

    Parameters:
        cities (DataFrame): city coordinates
        tour (list): initial tour order

    Returns:
        improved_tour, improved_length
    """
    best_tour = tour.copy()
    best_distance = calculate_total_distance(cities, best_tour)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour) - 1):
                # Reverse the segment between i and j
                new_tour = best_tour[:i] + best_tour[i:j][::-1] + best_tour[j:]
                new_distance = calculate_total_distance(cities, new_tour)

                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improved = True
                    break
            if improved:
                break

    return best_tour, best_distance


def tsp_kopt(cities, tour, k=3):
    """
    Simplified K-opt heuristic (iterative improvement).

    Parameters:
        cities (DataFrame)
        tour (list)
        k (int): number of edges to swap

    Returns:
        improved_tour, improved_length
    """
    best_tour = tour.copy()
    best_distance = calculate_total_distance(cities, best_tour)
    improved = True

    while improved:
        improved = False
        # For simplicity, we just apply multiple 2-opt style swaps
        # This approximates k-opt without exponential complexity
        for i in range(1, len(best_tour) - k):
            for j in range(i + k, len(best_tour) - 1):
                new_tour = best_tour[:i] + best_tour[i:j][::-1] + best_tour[j:]
                new_distance = calculate_total_distance(cities, new_tour)

                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improved = True
                    break
            if improved:
                break

    return best_tour, best_distance
