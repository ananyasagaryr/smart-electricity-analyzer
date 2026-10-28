import pandas as pd
import joblib

# Load cleaned dataset
data = pd.read_csv("clean_energy_data.csv")

# Load trained AI model
model = joblib.load("energy_model.pkl")

# Calculate average consumption
average_energy = data["Energy"].mean()

print("Average Energy Consumption:",
      round(average_energy, 2), "kWh")

# High consumption threshold
threshold = average_energy * 1.5

print("\nConsumption Analysis")
print("--------------------")

for energy in data["Energy"]:

    if energy > threshold:
        print("HIGH CONSUMPTION:",
              round(energy, 2), "kWh")
    else:
        print("NORMAL:",
              round(energy, 2), "kWh")


# -------------------------
# AI Prediction
# -------------------------

print("\nAI ENERGY PREDICTION")
print("--------------------")

# Take one row from the dataset
sample = data.iloc[[0]]

# Select features used by the model
features = sample[[
    "Hour",
    "Temperature",
    "Voltage",
    "Current",
    "Previous_Energy",
    "Power"
]]

# Predict energy consumption
prediction = model.predict(features)

print(
    "Predicted Energy Consumption:",
    round(prediction[0], 2),
    "kWh"
)