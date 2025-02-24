import pandas as pd
import great_expectations as ge
from great_expectations.data_context import get_context
from great_expectations.validator.validator import Validator
from great_expectations.execution_engine.pandas_execution_engine import PandasExecutionEngine
from great_expectations.core.batch import Batch, LegacyBatchDefinition, IDDict

# Load dataset
data = pd.read_csv("anomalies_detected.csv")

# ✅ Use get_context() to create an in-memory context
context = get_context(mode="ephemeral")

# ✅ Create an execution engine
execution_engine = PandasExecutionEngine()

# ✅ Create a batch (needed for Validator)
batch = Batch(
    data=data,
    batch_definition=LegacyBatchDefinition(
        datasource_name="my_pandas_datasource",
        data_connector_name="runtime_data_connector",
        data_asset_name="sales_data",
        batch_identifiers=IDDict({"default_identifier_name": "batch_1"}),
    )
)

# ✅ Create a Validator
validator = Validator(execution_engine=execution_engine, batches=[batch])

# ✅ Define validation rules with proper result_format
validator.expect_column_values_to_not_be_null("Customer_ID", result_format="SUMMARY")
validator.expect_column_values_to_not_be_null("Sales_Amount", result_format="SUMMARY")
validator.expect_column_values_to_be_unique("Transaction_ID", result_format="SUMMARY")
validator.expect_column_values_to_be_between("Sales_Amount", min_value=5, max_value=2000, result_format="SUMMARY")
validator.expect_column_values_to_match_regex("Email", r"[^@]+@[^@]+\.[^@]+", mostly=0.95, result_format="SUMMARY")

# ✅ Run validation
validation_results = validator.validate(result_format="SUMMARY")
print(validation_results)

# ✅ Save validation results
with open("validation_results.txt", "w") as f:
    f.write(str(validation_results))
