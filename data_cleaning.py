import pandas as pd

# Load the merged dataset from Step 1
merged_data = pd.read_csv('merged_dataset.csv')

# Convert categorical columns to string type before filling missing values
merged_data['Customer_Name'] = merged_data['Customer_Name'].astype('string')
merged_data['Email'] = merged_data['Email'].astype('string')
merged_data['City'] = merged_data['City'].astype('string')

# Handling missing categorical values
merged_data['Customer_Name'].fillna('Unknown', inplace=True)
merged_data['Email'].fillna('no-email@example.com', inplace=True)
merged_data['City'].fillna('Unknown City', inplace=True)

# Handling missing numerical values (impute with median)
numerical_columns = ['Sales_Amount', 'Price', 'Stock_Level']
for col in numerical_columns:
    if col in merged_data.columns:
        merged_data[col] = pd.to_numeric(merged_data[col], errors='coerce')  # Ensure numeric dtype
        merged_data[col].fillna(merged_data[col].median(), inplace=True)

# Display the cleaned dataset
print(merged_data.head())

# Save the cleaned dataset for further processing
merged_data.to_csv("cleaned_dataset.csv", index=False)
