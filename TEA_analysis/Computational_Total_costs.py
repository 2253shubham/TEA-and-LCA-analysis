import matplotlib.pyplot as plt

# Summary Comp
equipment = ["AEC", "Uti"]
costs = [4840.80/255, 4464.86/255]
total_cost = sum(costs)
colors = ["blue", "green"]  # Different colors for each contribution

# Create a stacked bar plot
plt.figure(figsize=(2.5, 6))
plt.bar("Proposed comp. costs", total_cost, color="white", edgecolor="black")  # Base bar
bottom = 0

# Add each component as a segment of the bar
for cost, label, color in zip(costs, equipment, colors):
    plt.bar("Proposed comp. costs", cost, bottom=bottom, label=label, color=color)
    bottom += cost

# Labels and title
#plt.ylabel("Benchmarking costs ($)", size = 16)
#plt.title("Benchmarking costs (OpEx) - Benchmark System")
#plt.legend(loc="upper right")

# **Increase tick mark size**
plt.tick_params(axis='y', which='major', labelsize=14, length=8, width=2)
plt.tick_params(axis='x', which='major', labelsize=14, length=8, width=2)
# Show the plot
plt.show()