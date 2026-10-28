import pandas as pd
import numpy as np

# To get the same dataset every time
np.random.seed(42)

# Number of records
n = 300

# -----------------------------
# Generate electricity data
# -----------------------------

# Hour of the day: 0 to 23
hour = np.random.randint(0, 24, n)

# Temperature in °C
temperature = np.random.uniform(20, 38, n)

# Voltage around 230 V
voltage = np.random.normal(230, 5, n)

# Current in Amperes
current = np.random.uniform(1, 15, n)

# Previous energy consumption in kWh
previous_energy = np.random.uniform(1, 10, n)

# Power in kW
power = (voltage * current) / 1000

# Energy consumption in kWh
energy = (
    0.4 * power
    + 0.2 * previous_energy
    + 0.03 * temperature
    + np.random.normal(0, 0.3, n)
)

# Make sure energy is positive
energy = np.maximum(energy, 0.5)

# -----------------------------
# Create DataFrame
# -----------------------------

data = pd.DataFrame({
    "Hour": hour,
    "Temperature": temperature,
    "Voltage": voltage,
    "Current": current,
    "Previous_Energy": previous_energy,
    "Power": power,
    "Energy": energy
})

# -----------------------------
# Add some missing values
# -----------------------------

data.loc[10, "Temperature"] = np.nan
data.loc[50, "Current"] = np.nan
data.loc[100, "Previous_Energy"] = np.nan
data.loc[150, "Voltage"] = np.nan

# -----------------------------
# Save as CSV
# -----------------------------

data.to_csv("energy_data.csv", index=False)

print("Dataset created successfully!")
print()
print("Number of rows:", len(data))
print("Number of columns:", len(data.columns))
print()
print(data.head(10))