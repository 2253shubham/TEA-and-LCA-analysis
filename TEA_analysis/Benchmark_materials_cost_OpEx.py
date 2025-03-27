import matplotlib.pyplot as plt

# Materials costs
equipment = ["Zeolites", "Hexadecane", "Hydrogen", "Argon", "Nitrogen"]
costs = [127.50/255, 8423.18/255, 1058.40/255, 814.80/255, 592.32/255]
total_cost = sum(costs)
colors = ["blue", "green", "orange", "purple", "magenta"]  # Different colors for each contribution

# Create a stacked bar plot
plt.figure(figsize=(2.5, 6))
plt.bar("Materials costs", total_cost, color="white", edgecolor="black")  # Base bar
bottom = 0

# Add each component as a segment of the bar
for cost, label, color in zip(costs, equipment, colors):
    plt.bar("Materials costs", cost, bottom=bottom, label=label, color=color)
    bottom += cost

# Labels and title
#plt.ylabel("Materials Cost ($)", size = 16)
#plt.title("Materials costs (OpEx) - Benchmark System")
#plt.legend(loc="upper right")

# **Increase tick mark size**
plt.tick_params(axis='y', which='major', labelsize=14, length=8, width=2)
plt.tick_params(axis='x', which='major', labelsize=14, length=8, width=2)
# Show the plot
plt.show()