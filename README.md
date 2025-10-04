# Traveling Salesman Problem (Heuristic Approaches)

This project implements and visualizes heuristic solutions to the **Traveling Salesman Problem (TSP)** using Python.  
It focuses on practical, scalable methods such as **Nearest Neighbor**, **Nearest Fragment (multi-start NN)**, and **Local Improvement** heuristics like **2-opt** and **k-opt**.

The goal is to balance **solution quality**, **runtime efficiency**, and **visual clarity**.

## Features

- **Nearest Neighbor (NN):** Greedy TSP heuristic starting from one city.
- **Nearest Fragment:** Runs NN from all starting points and returns the best path.
- **2-opt & k-opt (coming soon):** Local search improvements to refine tours.
- **Visual Output:** Routes plotted via `NetworkX` + `Matplotlib`.
- **Flexible Input:** Choose dataset size (`tiny.csv`, `small.csv`, `medium.csv`, `large.csv`).
- **Interactive CLI:** Menu-driven interface for choosing heuristics and datasets.

## Project Structure

```
TSP-Project/
│
├── dataset/
│ ├── tiny.csv
│ ├── small.csv
│ ├── medium.csv
│ └── large.csv
│
├── tsp_nn.py # Nearest Neighbor + Nearest Fragment heuristics
├── tsp_kopt.py # 2-opt and k-opt improvement algorithms
├── utils.py # Data loading, validation, and helper functions
├── main.py # Menu-driven interface for running heuristics
│
├── requirements.txt # Required Python libraries
└── README.md # Documentation
```

---

## Requirements

Before running the project, ensure you have **Python 3.8+** installed.

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Required Libraries
- `numpy`
- `matplotlib`
- `networkx`
- `pandas`

## How to Run

Run the program from the terminal or VS Code:
```
python main.py
```

You’ll see a **menu interface** like this:
```
=== TSP Heuristic Solver ===
1. Nearest Neighbor
2. Nearest Fragment
3. 2-opt Improvement
4. k-opt Improvement
0. Exit
Enter your choice:
```

Then you’ll be asked to select a dataset (`tiny.csv`, `small.csv`, etc.) and the number of cities to include.

After execution:

- The **tour** and its **total distance** are printed.
- A **visual plot** of the route is displayed.

## Example Output

```
Tour order (by city indices): [0, 2, 3, 1, 0]
Tour length: 12.45
```

And a neat plot of the tour will open showing the path connections.

## Future Extensions

Planned improvements:

- Add **random restarts** and **multi-start hybrid strategies**

- Add **benchmark comparison** on standard datasets

- Integrate **performance metrics** (runtime vs. quality plots)

- Improve visualization with **animation**

- **Optimize** distance computations (e.g., memoization)

