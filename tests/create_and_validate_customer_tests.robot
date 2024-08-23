*** Settings ***
Resource    ../resources/import.resource
Resource    ../resources/customer.resource


*** Variables ***
@{KEYS_CUSTOMER}    FirstName    LastName    Email    Phone


*** Test Cases ***
Create Customer data
    ${customer} =    Read Yaml File    ${DEFAULT_FILE_YAML_CUSTOMER}
    Log To Console    Creating a new instance of the Customer class
    Verify data before write to yaml    ${DEFAULT_FILE_CSV_CUSTOMER}    @{KEYS_CUSTOMER}
    Check Customer Exists    ${DEFAULT_FILE_CSV_CUSTOMER}    ${DEFAULT_FILE_YAML_CUSTOMER}    @{KEYS_CUSTOMER}
    Create Data Customer From Csv    ${DEFAULT_FILE_CSV_CUSTOMER}    ${DEFAULT_FILE_YAML_CUSTOMER}    @{KEYS_CUSTOMER}
    Verify data after write to yaml    ${customer}    @{KEYS_CUSTOMER}
