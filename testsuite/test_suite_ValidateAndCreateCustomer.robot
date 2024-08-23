*** Settings ***
Resource    ../resources/import.robot
Resource    ../resources/keyword_customer.robot


*** Variables ***
${KEYS_CUSTOMER}            FirstName    LastName    Email    Phone
${KEYS_CHECK_CUSTOMER}      Email    Phone


*** Test Cases ***
Create Customer
    ${data} =    Read Csv File    ${CSV_FILE_CUSTOMER}
    ${yaml_data} =    Read Yaml File    ${YAML_CUSTOMER}
    Log To Console    Creating a new instance of the Customer class
    Verify data before write to yaml    ${data}    @{KEYS_CUSTOMER}
    Check Customer Exists    ${CSV_FILE_CUSTOMER}    ${YAML_CUSTOMER}    @{KEYS_CHECK_CUSTOMER}
    Create Data Customer From Csv    ${CSV_FILE_CUSTOMER}    ${YAML_CUSTOMER}    @{KEYS_CHECK_CUSTOMER}
    Verify data after write to yaml    ${yaml_data}    @{KEYS_CUSTOMER}
