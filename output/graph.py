import matplotlib.pyplot as plt

# Values for running
sizes = [10, 30, 100, 1000]
time_nn = [0.0010, 0.0286, 0.1188, 13.0831]
time_nf = [0.0355, 0.3397, 12.6152, 20035.6476]
time_2opt = [0.0162, 1.0764, 180.4433, 220174.532]  
time_kopt = [0.0119, 0.7431, 108.2641, 93729.3641]

plt.figure(figsize=(8,5))
plt.plot(sizes, time_nn, marker='o', label='NN')
plt.plot(sizes, time_nf, marker='o', label='NF')
plt.plot(sizes, time_2opt, marker='o', label='2-Opt')
plt.plot(sizes, time_kopt, marker='o', label='k-Opt')

# Add a comment under the last point
plt.text(
    sizes[-1],                          # x-coordinate
    time_kopt[-1] / 2,                  # y-coordinate (a bit below)
    'Used k=5 instead of k=3',          # text
    ha='center', va='top',              # alignment
    fontsize=9, color='darkred'
)

plt.xscale('log')                               # Set x-axis to logarithmic scale for better scaling visualization
plt.yscale('log')                               # Set y-axis to logarithmic scale to show exponential growth clearly
plt.xlabel('Dataset size (n)')                  # Label for the x-axis
plt.ylabel('Time (seconds)')                    # Label for the y-axis
plt.title('Runtime scaling of heuristics vs dataset size')  # Add a descriptive title to the plot
plt.legend()                                    # Display legend showing which line corresponds to which heuristic
plt.grid(True, which="both", ls="--", linewidth=0.5)  # Add grid lines for both major and minor ticks, dashed and light
plt.tight_layout()                              # Adjust layout so labels/titles fit nicely without overlap
plt.show()                                      # Render and display the plot window

