import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load cleaned dataset
data = pd.read_csv("clean_energy_data.csv")

# Features
X = data[[
    "Hour",
    "Temperature",
    "Voltage",
    "Current",
    "Previous_Energy",
    "Power"
]]

# Target
y = data["Energy"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Save model
joblib.dump(model, "energy_model.pkl")

print("Model saved successfully!")

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMODEL RESULTS")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# Actual vs predicted
results = pd.DataFrame({
    "Actual Energy": y_test.values,
    "Predicted Energy": predictions
})

print("\nACTUAL VS PREDICTED")
print(results)