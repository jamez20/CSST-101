import os
import ssl
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Fix SSL certificate verification issue on macOS
ssl._create_default_https_context = ssl._create_unverified_context

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
CSV_PATH = os.path.join(DATA_DIR, "housing.csv")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(CSV_PATH):
    print("Downloading California Housing dataset...")
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame
    df.to_csv(CSV_PATH, index=False)
    print(f"Dataset saved to {CSV_PATH}")
else:
    print(f"Loading existing housing.csv file from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH)

print("\n===== DATASET EXPLORATION =====")
print("Shape of dataset:", df.shape)
print("Column names:", list(df.columns))
print("\nFirst 5 rows:\n", df.head())
print("\nSummary statistics:\n", df.describe())

print("\n--- MINI-TASK ANSWERS ---")
print("Input (features): median income, house age, average rooms, average bedrooms, "
      "population, average occupancy, latitude, longitude")
print("Output (label): median house value")
print("Type of learning: Supervised Learning (Regression)")

X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n===== TRAIN-TEST SPLIT =====")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\n===== MODEL TRAINING =====")
print("Baseline model: Linear Regression")
print("Training complete.")

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n===== MODEL EVALUATION =====")
print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")
print("This means the average prediction error is about "
      f"${rmse * 100000:.0f} per house when measured in dollars.")

print("\n===== REFLECTION & DISCUSSION =====")
print("Machine learning challenges observed include:")
print("1. Overfitting – when a model memorizes training data and fails to generalize.")
print("2. Underfitting – when a simple model (like Linear Regression) "
      "cannot capture complex relationships in the data.")
print("3. Bad data – missing or wrong values can cause inaccurate predictions.")

print("\nIf the dataset contained missing or incorrect values, "
      "the model’s predictions would be unreliable. Data cleaning "
      "and preprocessing are essential before training.")

print("\nIn real-world applications, models like this can help predict housing prices, "
      "guide real estate investments, or support government planning. "
      "However, success depends heavily on high-quality, representative data.")

print("\n===== SUMMARY =====")
print("ML Type Used: Supervised Learning (Regression)")
print(f"Model: Linear Regression | RMSE: {rmse:.3f}")
print("Possible Challenges: Underfitting, bad data quality, data bias.")
print("==============================================================")
