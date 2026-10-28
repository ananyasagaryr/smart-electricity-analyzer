import pandas as pd

# Load cleaned data
data = pd.read_csv("clean_energy_data.csv")

# Calculate average consumption
average_energy = data["Energy"].mean()

# Find highest consumption
highest_energy = data["Energy"].max()

print("AGENTIC AI RECOMMENDATION")
print("-------------------------")

print("Average Consumption:",
      round(average_energy, 2), "kWh")

print("Highest Consumption:",
      round(highest_energy, 2), "kWh")

# Agent decision-making
if highest_energy > average_energy * 1.5:

    print("\nAgent Decision:")
    print("High consumption detected.")

    print("\nRecommendation:")
    print("1. Check high-power electrical appliances.")
    print("2. Reduce unnecessary electricity usage.")
    print("3. Monitor consumption during peak hours.")

elif highest_energy > average_energy:

    print("\nAgent Decision:")
    print("Moderately high consumption detected.")

    print("\nRecommendation:")
    print("Monitor electricity usage and avoid unnecessary loads.")

else:

    print("\nAgent Decision:")
    print("Normal consumption detected.")

    print("\nRecommendation:")
    print("Continue monitoring electricity consumption.")