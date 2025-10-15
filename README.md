# Traveling Salesman Problem (Heuristic Approaches)

This project implements and visualizes heuristic solutions to the **Traveling Salesman Problem (TSP)** using Python.  
It focuses on practical, scalable methods such as **Nearest Neighbor**, **Nearest Fragment (multi-start NN)**, and **Local Improvement** heuristics like **2-opt** and **k-opt**.

The goal is to balance **solution quality**, **runtime efficiency**, and **visual clarity**.

## Features

- **Nearest Neighbor (NN):** Greedy TSP heuristic starting from one city.
- **Nearest Fragment:** Runs NN from all starting points and returns the best path.
- **Pairwise Exchange (2-opt) & k-opt:** Local search improvements to refine tours.
- **Visual Output:** Routes plotted via `NetworkX` + `Matplotlib`.
- **Flexible Input:** Choose dataset size (`tiny.csv`, `small.csv`, `medium.csv`, `large.csv`).
- **Interactive CLI:** Menu-driven interface for choosing heuristics and datasets.

## Project Structure

```
TSP-Project/
│
├── dataset/
│   ├── UK_Cities.csv
│   ├── Tourist places in Karnataka.xlsx
│   ├── Britain open_pubs.xlsx
│   └── Testing/
│       ├── tiny.csv
│       ├── small.csv
│       ├── medium.csv
│       └── large.csv
│
├── output/                             # Generated tours, plots & results
│
├── src/
│   ├── tsp_nn.py                       # Nearest Neighbour and Nearest Fragment
│   ├── tsp_kopt.py                     # K-opt (inlcudes Pairwise Exchange at k=2)
│   ├── utils.py                        # Helper funcs, like loading datasets, distance calc, 
│   │                                     plotting tours etc.
│   └── main.py                         # Menu-driven system combining everything
│
├── .gitignore                          # Ignore unnecessary files
├── LICENSE                             # License info (e.g., MIT)
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

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
>>> Enter your choice:
```

Once you select an algorithm to run (choosing _Option 4_ will end the program), you'd have another **menu** to choose the datasets
```
Choose a dataset:
1. UK_Cities.csv
2. England open_pubs.csv
3. Tourist places_Karnataka.csv
4. Testing dataset (tiny, small, medium, large)
0. Back to main menu
>>> Enter your choice:
```

Here you can choose between 3 real world datasets: `UK_Cities.csv`, `Tourist places_Karnataka.csv` and `England open_pubs.csv`. Additionally, there are 4 **test datasets** (`tiny.csv`, `small.csv`, etc.) of various sizes which can be used by _Option 4_.
```
Select Testing dataset:
1. tiny.csv
2. small.csv
3. medium.csv
4. large.csv
0. Back
>>> Enter your choice:
```

Additionally, if you choose _Option 4_, there would be input option for the **k-value**.
```
>>> Enter value of k for K-opt:
```

After execution:

- The **tour** and its **total distance** are printed.
- If choosing _Option 3_ or _Option 4_ of the **algorithm choosing menu**, it will also print the **initial tour distance** so as to evaluate the improvement.
- A **visual plot** of the route is displayed.
- The **time taken** as to run the whole algorithm with the selected dataset would be printed.

## Example Output

For computing _Options 1,2_
```
Tour order (by city indices): [0, 2, 3, 1, 0]
Tour length: 12.45
Execution time: 0.0001 seconds
```

or for _Options 3,4_
```
Improved tour (k-opt): [0, 2, 1, 3, 0]
Initial tour length (NN): 12.45
Improved tour length (2-Opt): 11.35
Execution time: 0.0121 seconds
```

And a neat plot of the tour will open showing the path connections.

## Future Extensions

Planned improvements:

- Add **benchmark comparison** on standard datasets

- Integrate **performance metrics** (runtime vs. quality plots)

- Improve visualization with **animation**

- **Optimize** distance computations (e.g., memoization)


### Authors: 
- [_Daibik Barik_](https://github.com/theikosB) (BMAT2316)
- [_Samadrita Bhattacharya_](https://github.com/Samadrita16) (BMAT2336)

**Team name:** _Almost Coders_