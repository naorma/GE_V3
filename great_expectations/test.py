from ruamel import yaml

import great_expectations as ge
from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest

context = ge.get_context()

# batch_request_query = BatchRequest(
#     datasource_name="sf_sso",
#     data_connector_name="default_inferred_data_connector_name",
#     data_asset_name="custom_sql_query",  # this is the name of the table you want to retrieve
#     data_connector_query='select distinct brand from(select brand, sum(SALES_VALUE)from SKUSALES_PROCESSEDgroup by brand)'
# )

batch_request = BatchRequest(
    datasource_name="sf_sso",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="skusales_processed",  # this is the name of the table you want to retrieve
)
context.create_expectation_suite(
    expectation_suite_name="skusales_processed_validations", overwrite_existing=True
)


def create_and_get_validetor():
    validator = context.get_validator(
        batch_request=batch_request, expectation_suite_name="skusales_processed_validations"
    )
    return validator



print(create_and_get_validetor().expect_column_values_to_not_be_null(column='brand'))
