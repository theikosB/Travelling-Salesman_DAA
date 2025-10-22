import matplotlib.pyplot as plt

# Example (replace with your actual values)
sizes = [10, 30, 100, 1000]
time_nn = [0.0012, 0.01, 0.3, 35.0]
time_2opt = [0.0025, 0.03, 2.5, 200.0]  # hypothetical

plt.figure(figsize=(8,5))
plt.plot(sizes, time_nn, marker='o', label='NN')
plt.plot(sizes, time_2opt, marker='o', label='2-Opt')
# you can add lines for NF, k-Opt too

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Dataset size (n)')
plt.ylabel('Time (seconds)')
plt.title('Runtime scaling of heuristics vs dataset size')
plt.legend()
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.tight_layout()
plt.savefig("runtime_scaling.png")
plt.show()
