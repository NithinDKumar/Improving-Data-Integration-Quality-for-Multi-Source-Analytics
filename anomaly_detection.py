from sklearn.ensemble import IsolationForest
import pandas as pd

# Load dataset
input_file = "cleaned_dataset.csv"
data = pd.read_csv(input_file)

# Select relevant numerical columns (modify as needed)
numerical_features = ["Sales_Amount", "Stock_Level", "Price"]  # Adjust based on dataset
data_filtered = data[numerical_features].dropna()

# Train Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
data_filtered["Anomaly_Score"] = model.fit_predict(data_filtered)

# Label anomalies (1 = Anomaly, 0 = Normal)
data_filtered["Predicted"] = (data_filtered["Anomaly_Score"] == -1).astype(int)

# Create "Actual" column for evaluation (Assuming all data is normal initially)
data_filtered["Actual"] = 0  # Later, manually mark known anomalies for evaluation

# Save results
output_file = "anomaly_results.csv"
data_filtered.to_csv(output_file, index=False)

print(f"Anomaly detection results saved to {output_file}")
