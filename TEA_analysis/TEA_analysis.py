import numpy as np

# Input Parameters (Example values, need real data)
core_hour_cost = 0.05  # Cost per core-hour in USD
hpc_nodes = 3           # Nodes per DFT calculation
hours_per_dft = 50      # Compute hours per DFT calculation
simultaneous_runs = 50  # Parallel simulations on HPC

total_zeolites = 255
selected_zeolites = 15
final_top_zeolites = 5
active_sites_per_zeolite = 5
reactions_per_zeolite = 14

# Experimental costs
experiment_cost_per_zeolite = 5000  # Estimated cost per experimental catalyst test

# Compute total computational cost
c4_dft_cost = core_hour_cost * hpc_nodes * hours_per_dft
c15_dft_cost = c4_dft_cost * (15 / 4)  # Extrapolated cost for C15 cracking

total_computational_cost = total_zeolites * active_sites_per_zeolite * reactions_per_zeolite * c15_dft_cost

total_experimental_cost = total_zeolites * experiment_cost_per_zeolite

# Payback period calculation
cost_savings_per_project = total_experimental_cost - total_computational_cost
payback_period = total_computational_cost / cost_savings_per_project

# Sensitivity Analysis (varying computational and experimental costs)
def sensitivity_analysis(cost_variation_range=np.linspace(0.8, 1.2, 5)):
    for factor in cost_variation_range:
        mod_comp_cost = total_computational_cost * factor
        mod_exp_cost = total_experimental_cost * factor
        mod_savings = mod_exp_cost - mod_comp_cost
        mod_payback = mod_comp_cost / mod_savings
        print(f"Factor: {factor:.2f}, Payback Period: {mod_payback:.2f} projects")

# Output Results
print(f"Total Computational Cost: ${total_computational_cost:,.2f}")
print(f"Total Experimental Cost: ${total_experimental_cost:,.2f}")
print(f"Payback Period: {payback_period:.2f} projects")

# Run sensitivity analysis
sensitivity_analysis()
