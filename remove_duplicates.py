import pandas as pd
from fuzzywuzzy import fuzz, process

# Load dataset
csv_file = "cleaned_dataset.csv"
data = pd.read_csv(csv_file)

# Ensure column name exists
column_name = "Customer_Name"
if column_name not in data.columns:
    raise KeyError(f"Column '{column_name}' not found in dataset.")

# Convert column to string and handle missing values
data[column_name] = data[column_name].astype(str).fillna("Unknown")

# Remove rows where Customer_Name is 'Unknown'
data = data[data[column_name] != "Unknown"]

# Identify duplicates using fuzzy matching
duplicates = []
seen = set()

for i, name in enumerate(data[column_name]):
    if name in seen:
        continue

    matches = process.extract(name, data[column_name], limit=10)  # Removed 'score_cutoff'
    
    for match_name, score, j in matches:
        if i != j and score > 85:  # Apply score threshold manually
            duplicates.append((i, j, score))
            seen.add(match_name)  # Mark as processed

# Print results
print("Duplicate Pairs:", duplicates)

# Save duplicate pairs to CSV
duplicates_df = pd.DataFrame(duplicates, columns=["Index_1", "Index_2", "Similarity_Score"])
duplicates_df.to_csv("duplicate_pairs.csv", index=False)

print("Duplicate pairs saved to duplicate_pairs.csv")
