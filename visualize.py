import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv("clean_energy_data.csv")

# -----------------------------
# Graph 1: Energy vs Hour
# -----------------------------

plt.figure(figsize=(8, 5))

plt.plot(data["Hour"], data["Energy"], "o")

plt.xlabel("Hour of Day")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Energy Consumption vs Hour")

plt.grid(True)
plt.show()


# -----------------------------
# Graph 2: Power vs Current
# -----------------------------

plt.figure(figsize=(8, 5))

plt.scatter(data["Current"], data["Power"])

plt.xlabel("Current (A)")
plt.ylabel("Power (kW)")
plt.title("Power vs Current")

plt.grid(True)
plt.show()


# -----------------------------
# Graph 3: Temperature vs Energy
# -----------------------------

plt.figure(figsize=(8, 5))

plt.scatter(data["Temperature"], data["Energy"])

plt.xlabel("Temperature (°C)")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Temperature vs Energy Consumption")

plt.grid(True)
plt.show()