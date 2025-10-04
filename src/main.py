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
        print("1. Nearest Neighbor Algorithm")
        print("2. Nearest Fragment (Multi Start) Operator")
        # Later add: 3. 2-opt, 4.k-opt (Make them in the same program file tsp_kopt.py)
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting program... Goodbye!")
            break


        elif choice == "0":
            dataset_path = choose_dataset()
            cities = load_cities(dataset_path)

            tour, total_length = tsp_nearest_neighbor(cities)
            print("\nTour order (by city indices):", tour)
            print("Tour length:", round(total_length, 2))

            plot_tour(cities, tour, title="TSP Tour (Nearest Neighbor)")


        elif choice == "2":
            dataset_path = choose_dataset()
            cities = load_cities(dataset_path)

            tour, total_length = tsp_nearest_fragment(cities)
            print("\nBest tour (multi-start NN):", tour)
            print("Best tour length:", round(total_length, 2))

            plot_tour(cities, tour, title="TSP Tour (Nearest Fragment)")
        

        elif choice == "3":
            tour, total_length = tsp_nearest_fragment(cities)
            improved_tour, improved_length = tsp_2opt(cities, tour)


        elif choice == "4":
            tour, total_length = tsp_nearest_fragment(cities)
            improved_tour, improved_length = tsp_kopt(cities, tour, k=3)
                        

        else:
            print("Invalid choice. Please try again.")
