import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Load your training data to get the unique values
df = pd.read_csv('garments_worker_productivity.csv')

# Clean the data - handle the space in 'finishing '
df['department'] = df['department'].str.strip()

# Extract unique values for each categorical column
unique_values = {
    'department': sorted(df['department'].unique().tolist()),
    'day': sorted(df['day'].unique().tolist()),
    'quarter': sorted(df['quarter'].unique().tolist())
}

print("Found unique values:")
for col, values in unique_values.items():
    print(f"  {col}: {values}")

# Save the preprocessor information
preprocessor = {
    'unique_values': unique_values
}

with open('preprocessor.pkl', 'wb') as f:
    pickle.dump(preprocessor, f)

print("\nPreprocessor saved successfully as 'preprocessor.pkl'")