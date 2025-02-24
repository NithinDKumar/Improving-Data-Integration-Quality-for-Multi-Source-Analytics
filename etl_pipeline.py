import pandas as pd
import os
from sklearn.ensemble import IsolationForest
from fuzzywuzzy import fuzz, process
from datetime import datetime

# Data Extraction
def extract_data(file_path="cleaned_dataset.csv"):
    """Extracts data from a CSV file."""
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        print("Data successfully loaded from:", file_path)
    else:
        raise FileNotFoundError(f"File {file_path} not found!")
    
    return data


# Data cleaning and duplicate rempval
def clean_data(data, text_columns=["Customer_Name", "Email", "City"]):
    """Removes duplicates and applies fuzzy matching."""
    
    # Drop exact duplicates
    data.drop_duplicates(inplace=True)

    # Apply fuzzy matching for near-duplicates
    duplicate_pairs = []
    for column_name in text_columns:
        if column_name in data.columns:
            unique_values = data[column_name].dropna().unique()
            for i, value in enumerate(unique_values):
                for j, other_value in enumerate(unique_values):
                    if i != j and fuzz.ratio(str(value), str(other_value)) > 85:
                        duplicate_pairs.append((value, other_value))
    
    print(f"Found {len(duplicate_pairs)} potential duplicate pairs.")
    return data


# Anomaly detection
def detect_anomalies(data, numeric_columns=["Sales_Amount", "Stock_Level", "Price"]):
    """Detects anomalies using Isolation Forest."""
    
    if not set(numeric_columns).issubset(data.columns):
        raise KeyError("Missing required numerical columns in dataset.")

    model = IsolationForest(contamination=0.05, random_state=42)  # Adjust contamination if needed
    anomaly_scores = model.fit_predict(data[numeric_columns])
    
    data["Anomaly"] = (anomaly_scores == -1).astype(int)  # Flag anomalies (1 = anomaly, 0 = normal)
    print(f"Detected {data['Anomaly'].sum()} anomalies.")
    
    return data


# Data storage
def save_cleaned_data(data, output_file="cleaned_final_dataset.csv"):
    """Saves the cleaned and processed data to a CSV file."""
    data.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")


# Etl-Pipeline
def run_etl_pipeline():
    """Executes the complete ETL pipeline."""
    
    print("\nStarting ETL Pipeline...\n")
    # Step 1: Extract Data
    raw_data = extract_data()
    # Step 2: Clean Data
    cleaned_data = clean_data(raw_data)
    # Step 3: Detect Anomalies
    processed_data = detect_anomalies(cleaned_data)
    # Step 4: Save the cleaned dataset
    save_cleaned_data(processed_data)

    print("\nETL Pipeline completed successfully!")


# Run pipeline
if __name__ == "__main__":
    run_etl_pipeline()
