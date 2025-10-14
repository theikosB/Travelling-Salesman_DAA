from utils import calculate_total_distance


def tsp_kopt(cities, tour, k=2):
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
