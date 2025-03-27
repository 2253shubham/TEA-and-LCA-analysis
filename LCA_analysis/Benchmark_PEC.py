import matplotlib.pyplot as plt

# PEC benchmark
equipment = ["Transp", "Parr", "cal", "X", "GC", "TP"]
costs = [18000*2.86/255, 18360*2.86/255, 6120*2.86/255, 143.44*2.86/255, 191.25*2.86/255, 255*2.86/255]
costs = [i *3412.24/1000000 for i in costs]
total_cost = sum(costs)
colors = ["blue", "green", "orange", "purple", "magenta", "cyan"]  # Different colors for each contribution

# Create a stacked bar plot
plt.figure(figsize=(2.5, 6))
plt.bar("Primary energy consumption", total_cost, color="white", edgecolor="black")  # Base bar
bottom = 0

# Add each component as a segment of the bar
for cost, label, color in zip(costs, equipment, colors):
    plt.bar("Primary energy consumption", cost, bottom=bottom, label=label, color=color)
    bottom += cost

# Labels and title
#plt.ylabel("Materials Cost ($)", size = 16)
#plt.title("Primary energy consumption (OpEx) - Benchmark System")
#plt.legend(loc="upper right")

# **Increase tick mark size**
plt.tick_params(axis='y', which='major', labelsize=14, length=8, width=2)
plt.tick_params(axis='x', which='major', labelsize=14, length=8, width=2)
# Show the plot
plt.show()