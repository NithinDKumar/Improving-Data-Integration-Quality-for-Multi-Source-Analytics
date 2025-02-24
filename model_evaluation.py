import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# Load actual and predicted anomalies from Isolation Forest
anomalies_csv = "anomaly_results.csv"  # This should contain actual and predicted anomalies
anomalies_data = pd.read_csv(anomalies_csv)

# Ensure necessary columns exist
if "Actual" not in anomalies_data.columns or "Predicted" not in anomalies_data.columns:
    raise KeyError("The file must contain 'Actual' and 'Predicted' columns.")

# Extract actual and predicted labels
actual = anomalies_data["Actual"]
predicted = anomalies_data["Predicted"]

# Compute Precision, Recall, and F1-score for Anomaly Detection
precision = precision_score(actual, predicted)
recall = recall_score(actual, predicted)
f1 = f1_score(actual, predicted)

print(f"Anomaly Detection - Precision: {precision:.2f}, Recall: {recall:.2f}, F1-score: {f1:.2f}")

# Load duplicate matching results
duplicates_csv = "duplicate_pairs.csv"  # This file is from `remove_duplicates.py`
duplicates_data = pd.read_csv(duplicates_csv)

# Compute Match Accuracy
total_pairs = len(duplicates_data)
correct_matches = duplicates_data[duplicates_data["Similarity_Score"] > 85].shape[0]
match_accuracy = correct_matches / total_pairs if total_pairs > 0 else 0

# False Positive Rate: Count incorrect matches (assuming threshold above 85)
false_positives = total_pairs - correct_matches
false_positive_rate = false_positives / total_pairs if total_pairs > 0 else 0

print(f"Duplicate Detection - Match Accuracy: {match_accuracy:.2f}, False Positive Rate: {false_positive_rate:.2f}")
