import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate normal data (random values within a range)
normal_data = pd.DataFrame({
    'Transaction_Amount': np.random.normal(loc=100, scale=20, size=1000),  # Normal distribution
    'Transaction_Duration': np.random.normal(loc=5, scale=1, size=1000)     # Normal transaction times
})

# Generate anomalies (extreme high values)
anomalies = pd.DataFrame({
    'Transaction_Amount': np.random.uniform(500, 1000, size=10),  # Extreme amounts
    'Transaction_Duration': np.random.uniform(15, 50, size=10)    # Unusually long durations
})

# Combine normal data with anomalies
dataset = pd.concat([normal_data, anomalies], ignore_index=True)

# Save dataset to CSV
dataset.to_csv("synthetic_transactions.csv", index=False)
print("Synthetic dataset generated and saved as 'synthetic_transactions.csv'")
