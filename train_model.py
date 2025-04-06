import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# ✅ Correct path to your CSV file
df = pd.read_csv('data/ice_cream_sales.csv')

# Clean column names
df.columns = df.columns.str.strip().str.title()

# Print column names
print("📋 Columns:", df.columns.tolist())

# Prepare features and target
X = df[['Temperature']]
y = df['Ice Cream Profits']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save trained model
os.makedirs('model', exist_ok=True)
with open('model/linear_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as model/linear_model.pkl")
