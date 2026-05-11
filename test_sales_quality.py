import pandas as pd
import great_expectations as gx
import warnings
import os

# Disable warnings / progress bars
warnings.filterwarnings("ignore")
os.environ["TQDM_DISABLE"] = "1"

# Wczytanie danych
df = pd.read_csv("sales_2024_01.csv")

# GX Context
context = gx.get_context()

# Create Expectation Suite
suite_name = "sales_quality_suite"

try:
    context.suites.add(
        gx.ExpectationSuite(name=suite_name)
    )
except Exception:
    # Suite already exists
    pass

# Create datasource
datasource = context.data_sources.add_pandas(
    name="my_pandas_datasource"
)

# Create dataframe asset
data_asset = datasource.add_dataframe_asset(
    name="sales_data"
)

# Batch definition
batch_definition = data_asset.add_batch_definition_whole_dataframe(
    name="batch_definition"
)

# Create batch
batch = batch_definition.get_batch(
    batch_parameters={
        "dataframe": df
    }
)

# Create validator
validator = context.get_validator(
    batch=batch,
    expectation_suite_name=suite_name
)

# Expectations
validator.expect_column_values_to_not_be_null(
    "order_id"
)

validator.expect_column_values_to_be_unique(
    "order_id"
)

validator.expect_column_values_to_match_strftime_format(
    "order_date",
    "%Y-%m-%d"
)

validator.expect_column_values_to_be_between(
    "amount",
    0
)

validator.expect_column_values_to_be_in_set(
    "currency",
    ["PLN", "EUR", "USD"]
)

# Run validation
results = validator.validate()

# Print summary
print("\n=== VALIDATION RESULTS ===\n")
print("Overall Success:", results.success)

# Detailed results
for res in results.results:
    print(f"\nExpectation: {res.expectation_config.type}")
    print("Success:", res.success)