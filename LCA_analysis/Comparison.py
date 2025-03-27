import matplotlib.pyplot as plt
import numpy as np

# Data for the stacked bars
equipment1 = ["LS", "PC", "HPC"]
costs1 = [1.76/255, 175.60/255, 12.29/255]  # New costs
equipment2 = ["Ts", "Pa", "Cc", "X", "GC", "TP"]
costs2 = [0.69, 0.70, 0.23, 0.005, 0.007, 0.01]  # Old costs
colors1 = ["blue", "green", "orange"]
colors2 = ["blue", "green", "orange", "purple", "magenta", "cyan"]

# Bar positions
bar_width = 0.8
index = np.arange(2)  # Two bars: new and old
#index[1] = index[0] + bar_width/2 + 0.1

# Create the figure and axes
fig, ax = plt.subplots(figsize=(5, 6))

# Create the first stacked bar (New)
bottom = 0
for cost, color in zip(costs1, colors1):
    ax.bar(index[0], cost, bar_width, bottom=bottom, color=color)
    bottom += cost

# Create the second stacked bar (Old)
bottom = 0
for cost, color in zip(costs2, colors2):
    ax.bar(index[1], cost, bar_width, bottom=bottom, color=color)
    bottom += cost

# Customize the plot
ax.set_xticks(index)
ax.set_xticklabels(["Computational\nScreening", "Experimental\nScreening"])
plt.xticks(rotation=0, ha='center')
ax.tick_params(axis='y', which='major', labelsize=14, length=8, width=2)
ax.tick_params(axis='x', which='major', labelsize=14, length=8, width=2)

plt.tight_layout()
plt.show()