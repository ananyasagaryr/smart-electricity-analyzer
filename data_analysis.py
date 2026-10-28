import pandas as pd

# Load dataset
data = pd.read_csv("energy_data.csv")

# Show first 5 rows
print("FIRST 5 ROWS:")
print(data.head())

# Check dataset information
print("\nDATASET INFORMATION:")
print(data.info())

# Check missing values
print("\nMISSING VALUES:")
print(data.isnull().sum())

# Fill missing numerical values with median
data = data.fillna(data.median(numeric_only=True))

# Check again
print("\nMISSING VALUES AFTER CLEANING:")
print(data.isnull().sum())

# Save cleaned dataset
data.to_csv("clean_energy_data.csv", index=False)

print("\nDataset cleaned successfully!")