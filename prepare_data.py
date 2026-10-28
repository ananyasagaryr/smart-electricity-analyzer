import pandas as pd

# Load dataset
data = pd.read_csv("energy_data.csv")

print("BEFORE CLEANING")
print(data.isnull().sum())

# Fill missing values with median
data = data.fillna(data.median(numeric_only=True))

# Calculate electrical power
data["Power"] = (data["Voltage"] * data["Current"]) / 1000

print("\nAFTER CLEANING")
print(data.isnull().sum())

print("\nUPDATED DATASET")
print(data.head())

# Save the prepared dataset
data.to_csv("clean_energy_data.csv", index=False)

print("\nDataset prepared successfully!")