import matplotlib.pyplot as plt

# Operating cost of equipments
equipment = ["Parr Reactor", "Calcination Furnace", "XRD Analysis", "GC-MS", "TPD System"]
costs = [4123.66/255, 1374.55/255, 2550/255, 85.94/255, 57.26/255]
total_cost = sum(costs)
colors = ["blue", "green", "orange", "purple", "magenta"]  # Different colors for each contribution

# Create a stacked bar plot
plt.figure(figsize=(2.5, 6))
plt.bar("Utilities cost", total_cost, color="white", edgecolor="black")  # Base bar
bottom = 0

# Add each component as a segment of the bar
for cost, label, color in zip(costs, equipment, colors):
    plt.bar("Utilities cost", cost, bottom=bottom, label=label, color=color)
    bottom += cost

# Labels and title
#plt.ylabel("Utilities Cost ($)", size = 16)
#plt.title("Utilities costs (OpEx) - Benchmark System")
#plt.legend(loc="upper right")

# **Increase tick mark size**
plt.tick_params(axis='y', which='major', labelsize=14, length=8, width=2)
plt.tick_params(axis='x', which='major', labelsize=14, length=8, width=2)
# Show the plot
plt.show()