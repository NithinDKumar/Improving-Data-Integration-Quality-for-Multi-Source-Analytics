import pandas as pd

# Sample dataset with similar names
data = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': ['John Smith', 'Jon Smyth', 'Jane Doe', 'J. Smith', 'Janie Doe', 'Joan Smyth'],
    'Email': ['john@example.com', 'jon@example.com', 'jane@example.com', 'john.smith@example.com', 'janed@example.com', 'joan@example.com']
})

# Save dataset
data.to_csv("synthetic_duplicates.csv", index=False)
print("Synthetic duplicate dataset saved as 'synthetic_duplicates.csv'")
