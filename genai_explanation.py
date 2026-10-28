import pandas as pd

# Load data
data = pd.read_csv("clean_energy_data.csv")

# Calculate average
average_energy = data["Energy"].mean()

# Find highest consumption
highest_energy = data["Energy"].max()

# Find corresponding row
highest_row = data.loc[data["Energy"].idxmax()]

print("GENAI ENERGY EXPLANATION")
print("------------------------")

print("Average Energy Consumption:",
      round(average_energy, 2), "kWh")

print("Highest Energy Consumption:",
      round(highest_energy, 2), "kWh")

print("\nAI Explanation:")

if highest_energy > average_energy * 1.5:

    print(
        "Energy consumption is significantly higher than the average. "
        "The increased current and power demand may be contributing "
        "to the higher electricity consumption."
    )

else:

    print(
        "Energy consumption is within the normal range "
        "compared with the average."
    )