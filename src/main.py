import utils, tsp_nn, tsp_kopt

if __name__ == "__main__":
    while True:
        print(
            "Choose an option to do:\n",
            "1. TSP Heuristic with Nearest Fragment\n",
            "2. TSP with K-opt Heuristic"
        )
        tsp_choice = int(input("Your Choice: "))
        if tsp_choice == 2:
            k = int(input("Enter the k value to optimize: "))

            