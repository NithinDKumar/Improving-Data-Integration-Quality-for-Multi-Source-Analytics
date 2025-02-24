import pandas as pd

# Load datasets
customer_data = pd.read_csv('customer_data.csv')
sales_transactions = pd.read_csv('sales_transactions.csv')
inventory_product = pd.read_csv('inventory_product.csv')

# Schema Mapping (Renaming columns to match)
customer_data.rename(columns={'Name': 'Customer_Name'}, inplace=True)

# Merging sales data with customer data
merged_sales = pd.merge(sales_transactions, customer_data, on='Customer_ID', how='left')

# Merging with inventory data
final_merged_data = pd.merge(merged_sales, inventory_product, on='Product_ID', how='left')

# Display the merged dataset
print(final_merged_data.head())

# Save the merged dataset
final_merged_data.to_csv("merged_dataset.csv", index=False)
