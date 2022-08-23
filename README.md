# GE_V3

This is a small installation of great expectations 
It contains an sso connection to snowflake that needs to be modified by replacing the following configurations in the `great_expectations.yml` to your own:
  1. yours.snowflake.hostname
  2. yours.username.to.snowflake
  3. yours.database.name
  4. yours.database.query.schema
  5. yours.snowflake.role

This repo have also a checkpoint allready configored with a connection to datahub, this needs to be modified by configure the `my_checkpoint.yml` file as followed:
  1. change the `<server_ip>` to your datahub ip (you can remove this action if in is not neccesery)
  2. change the name of `expectation_suite_name` (in this repo it is 'skusales_processed_validations')
