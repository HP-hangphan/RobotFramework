*** Settings ***
Resource    ../resources/import.resource
Resource    ../resources/user.resource


*** Variables ***
@{KEYS}             Username    Password    Email
@{KEYS_CHECK}       Username    Email


*** Test Cases ***
Create user
    ${data} =    Read Csv File    ${DEFAULT_FILE_CSV_USER}
    ${yaml_data} =    Read Yaml File    ${DEFAULT_FILE_YAML_USER}
    Log To Console    Creating a new instance of the Customer class
    Verify data before write to yaml    ${data}    @{KEYS}
    Check User exists    ${DEFAULT_FILE_CSV_USER}    ${DEFAULT_FILE_YAML_USER}    @{KEYS_CHECK}
    Create data user from Csv    ${DEFAULT_FILE_CSV_USER}    ${DEFAULT_FILE_YAML_USER}    @{KEYS_CHECK}
    Verify data after write to yaml    ${yaml_data}    @{KEYS}
