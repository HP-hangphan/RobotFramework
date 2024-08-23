*** Settings ***
Resource    ../resources/import.robot
Resource    ../resources/keyword_user.robot


*** Variables ***
${CSV_FILE_USER}    ${CURDIR}/../data/users.csv
${YAML_USER}        ${CURDIR}/../output/data_user.yaml
@{KEYS}             Username    Password    Email
@{KEYS_CHECK}       Username    Email


*** Test Cases ***
Create user
    ${data} =    Read Csv File    ${CSV_FILE_USER}
    ${yaml_data} =    Read Yaml File    ${YAML_USER}
    Log To Console    Creating a new instance of the Customer class
    Verify data before write to yaml    ${data}    @{KEYS}
    Check User exists    ${CSV_FILE_USER}    ${YAML_USER}    @{KEYS_CHECK}
    Create data user from Csv    ${CSV_FILE_USER}    ${YAML_USER}    @{KEYS_CHECK}
    Verify data after write to yaml    ${yaml_data}    @{KEYS}
