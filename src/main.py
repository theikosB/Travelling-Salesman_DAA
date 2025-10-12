import time
from utils import load_cities
from tsp_nn import tsp_nearest_neighbor, tsp_nearest_fragment, plot_tour
from tsp_kopt import tsp_2opt, tsp_kopt

def timed_run(fn, *args):
    """
    Run a function and print its execution time.
    Parameters: the function to run, the arguments
    Returns whatever the function returns.
    """
    start = time.time()
    result = fn(*args)
    end = time.time()
    elapsed = end - start
    return result, elapsed

def choose_dataset():
    """Menu to select dataset file."""
    print("\nChoose a dataset:")
    print("1. tiny.csv")
    print("2. small.csv")
    print("3. medium.csv")
    print("4. large.csv")

    dataset_map = {
        "1": "dataset/tiny.csv",
        "2": "dataset/small.csv",
        "3": "dataset/medium.csv",
        "4": "dataset/large.csv"
    }

    while True:
        choice = input("Enter your choice: ")
        if choice in dataset_map:
            return dataset_map[choice]
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    while True:
        print("\n==== Traveling Salesman Problem Heuristics ====")
        print("1. Nearest Neighbor Algorithm")
        print("2. Nearest Fragment (Multi Start) Operator")
        print("3. Pairwise Exchange (2-opt)")
        print("4. (Inspired by) Lin–Kernighan heuristics")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting program... Goodbye!")
            break


        elif choice == "1":
            dataset_path = choose_dataset()
            cities = load_cities(dataset_path)

            tour, total_length = timed_run(tsp_nearest_neighbor, cities)

            print("\nTour order (by city indices):", tour)
            print("Tour length:", round(total_length, 2))
            print(f"Execution time: {elapsed:.4f} seconds")

            plot_tour(cities, tour, title="TSP Tour (Nearest Neighbor)")


        elif choice == "2":
            dataset_path = choose_dataset()
            cities = load_cities(dataset_path)

            tour, total_length = timed_run(tsp_nearest_fragment, cities)
            
            print("\nBest tour (multi-start NN):", tour)
            print("Best tour length:", round(total_length, 2))
            print(f"Execution time: {elapsed:.4f} seconds")
            plot_tour(cities, tour, title="TSP Tour (Nearest Fragment)")
        

        elif choice == "3":
            dataset_path = choose_dataset()
            cities = load_cities(dataset_path)

            tour, total_length = tsp_nearest_neighbor(cities)
            improved_tour, improved_length = timed_run(tsp_2opt, cities, tour)

            print(f"Initial tour length (NN): {round(total_length, 2)}")
            print(f"Improved tour length (2-Opt): {round(improved_length, 2)}")
            print(f"Execution time: {elapsed:.4f} seconds")
            plot_tour(cities, improved_tour)


        elif choice == "4":
            dataset_path = choose_dataset()
            cities = load_cities(dataset_path)

            tour, total_length = tsp_nearest_neighbor(cities)
            k_value = int(input("Enter value of k for K-opt: "))
            
            improved_tour, improved_length = timed_run(tsp_kopt, cities, tour, k_value)

            print(f"Initial tour length (NN): {round(total_length, 2)}")
            print(f"Improved tour length (K-Opt, k=3): {round(improved_length, 2)}")
            print(f"Execution time: {elapsed:.4f} seconds")
            plot_tour(cities, improved_tour)
                        

        else:
            print("Invalid choice. Please try again.")
