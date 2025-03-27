import matplotlib.pyplot as plt

# Equipment and their amortized costs
equipment = ["Parr Reactor", "Calcination Furnace", "GC-MS", "TPD System"]
costs = [838.36/255, 838.36/255, 174.86 * 2/255, 465.75/255]
total_cost = sum(costs)
colors = ["blue", "green", "orange", "purple"]  # Different colors for each contribution

# Create a stacked bar plot
plt.figure(figsize=(2.5, 6))
plt.bar("Equipment Cost", total_cost, color="white", edgecolor="black")  # Base bar
bottom = 0

# Add each component as a segment of the bar
for cost, label, color in zip(costs, equipment, colors):
    plt.bar("Equipment Cost", cost, bottom=bottom, label=label, color=color)
    bottom += cost

# Labels and title
#plt.ylabel("Amortized Cost ($)", size = 16)
#plt.title("Amortized Equipment Costs (CapEx) - Benchmark System")
#plt.legend(loc="upper right")

# **Increase tick mark size**
plt.tick_params(axis='y', which='major', labelsize=14, length=8, width=2)
plt.tick_params(axis='x', which='major', labelsize=14, length=8, width=2)
# Show the plot
plt.show()