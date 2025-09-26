from utils import load_cities
from tsp_nn import tsp_nearest_neighbor, plot_tour

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
        print("1. Nearest Neighbor Heuristic")
        # Later add: 2. k-opt
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dataset_path = choose_dataset()
            cities = load_cities(dataset_path)

            tour, total_length = tsp_nearest_neighbor(cities)
            print("\nTour order (by city indices):", tour)
            print("Tour length:", round(total_length, 2))

            plot_tour(cities, tour, title="TSP Tour (Nearest Neighbor)")

        elif choice == "0":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
