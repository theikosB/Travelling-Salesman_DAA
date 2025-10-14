import time
from utils import load_cities, plot_tour
from tsp_nn import tsp_nearest_neighbor, tsp_nearest_fragment
from tsp_kopt import tsp_kopt

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
    """Unified menu to select dataset file (Real-world + Testing)."""

    real_map = {
        
        "1": "dataset/UK_Cities.csv",
        "2": "dataset/England open_pubs.csv",
        "3": "dataset/Tourist places_Karnataka.csv"
    }

    test_map = {
        "1": "dataset/Testing/tiny.csv",
        "2": "dataset/Testing/small.csv",
        "3": "dataset/Testing/medium.csv",
        "4": "dataset/Testing/large.csv"
    }

    while True:
        print("\nChoose a dataset:")
        print("1. UK_Cities.csv")
        print("2. England open_pubs.csv")
        print("3. Tourist places_Karnataka.csv")
        print("4. Testing dataset (tiny, small, medium, large)")
        print("0. Back to main menu")
        main_choice = input("Enter your choice: ")

        if main_choice in real_map:
            return real_map[main_choice]

        elif main_choice == "4":
            # Submenu for Testing datasets
            while True:
                print("\nSelect Testing dataset:")
                print("1. tiny.csv")
                print("2. small.csv")
                print("3. medium.csv")
                print("4. large.csv")
                print("0. Back")

                sub_choice = input("Enter your choice: ")

                if sub_choice in test_map:
                    return test_map[sub_choice]
                elif sub_choice == "0":
                    break  # Return to the main dataset menu
                else:
                    print("Invalid choice. Please try again.")

        elif main_choice == "0":
            return None  # Go back to main menu

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
            if dataset_path is None:
                continue  # Go back to main algorithm menu
            cities = load_cities(dataset_path)

            tour, total_length, elapsed = None, None, None

            result, elapsed = timed_run(tsp_nearest_neighbor, cities)
            tour, total_length = result  # unpack the result from your tsp function

            print("\nTour order (by city indices):", tour)
            print("Tour length:", round(total_length, 2))
            print(f"Execution time: {elapsed:.4f} seconds")

            plot_tour(cities, tour, title="TSP Tour (Nearest Neighbor)")


        elif choice == "2":
            dataset_path = choose_dataset()
            if dataset_path is None:
                continue  # Go back to main algorithm menu
            cities = load_cities(dataset_path)

            tour, total_length, elapsed = None, None, None

            result, elapsed = timed_run(tsp_nearest_fragment, cities)
            tour, total_length = result  # unpack the result from your tsp function
            
            print("\nBest tour (multi-start NN):", tour)
            print("Best tour length:", round(total_length, 2))
            print(f"Execution time: {elapsed:.4f} seconds")
            plot_tour(cities, tour, title="TSP Tour (Nearest Fragment)")
        

        elif choice == "3":
            dataset_path = choose_dataset()
            if dataset_path is None:
                continue  # Go back to main algorithm menu
            cities = load_cities(dataset_path)

            # Measure NN time
            (tour, total_length), elapsed_nn = timed_run(tsp_nearest_neighbor, cities)
            # Measure 2-opt time
            (improved_tour, improved_length), elapsed_opt = timed_run(tsp_kopt, cities, tour)

            total_elapsed = elapsed_nn + elapsed_opt

            print("\nImproved tour (2-opt):", improved_tour)
            print(f"Initial tour length (NN): {round(total_length, 2)}")
            print(f"Improved tour length (2-Opt): {round(improved_length, 2)}")
            print(f"Execution time: {total_elapsed:.4f} seconds")
            plot_tour(cities, improved_tour)


        elif choice == "4":
            dataset_path = choose_dataset()
            if dataset_path is None:
                continue  # Go back to main algorithm menu
            cities = load_cities(dataset_path)

            # Measure NN time
            (tour, total_length), elapsed_nn = timed_run(tsp_nearest_neighbor, cities)
            # Measure K-opt time
            k_value = int(input("\nEnter value of k for K-opt: "))
            (improved_tour, improved_length), elapsed_opt = timed_run(tsp_kopt, cities, tour, k_value)

            total_elapsed = elapsed_nn + elapsed_opt

            print(f"\nImproved tour ({k_value}-opt): {improved_tour}")
            print(f"Initial tour length (NN): {round(total_length, 2)}")
            print(f"Improved tour length (K-Opt, k=3): {round(improved_length, 2)}")
            print(f"Execution time: {total_elapsed:.4f} seconds")
            plot_tour(cities, improved_tour)
                        

        else:
            print("\nInvalid choice. Please try again.")
