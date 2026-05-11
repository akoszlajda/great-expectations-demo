import pandas as pd
import great_expectations as gx
import warnings
import os

warnings.filterwarnings("ignore")
os.environ["TQDM_DISABLE"] = "1"

# Przykładowe dane
df = pd.DataFrame({
    "name": ["Adam", "Kasia", "Jan"],
    "age": [34, 15, 28],
    "email": ["adam@test.com", None, "jan-test.com"]
})

# Tworzenie GX context
context = gx.get_context()

# Tworzenie Expectation Suite
suite = context.suites.add(
    gx.ExpectationSuite(
        name="test_suite"
    )
)

# Tworzenie datasource
datasource = context.data_sources.add_pandas(
    name="my_pandas_datasource"
)

# Tworzenie assetu
data_asset = datasource.add_dataframe_asset(
    name="sales_data"
)

# Batch definition
batch_definition = data_asset.add_batch_definition_whole_dataframe(
    "batch_definition"
)

# Pobranie batcha
batch = batch_definition.get_batch(
    batch_parameters={"dataframe": df}
)

# Validator
validator = context.get_validator(
    batch=batch,
    expectation_suite_name="test_suite"
)

# Expectations
result1 = validator.expect_column_values_to_not_be_null(
    "email"
)

result2 = validator.expect_column_values_to_be_between(
    "age",
    min_value=18
)

result3 = validator.expect_column_values_to_match_regex(
    "email",
    r".+@.+"
)

# Wyniki
print("\n=== WYNIKI WALIDACJI ===\n")

for result in [result1, result2, result3]:
    print(result.expectation_config.type)
    print("Success:", result.success)
    print(result.result)
    print("-" * 50)