*** Settings ***
Library    /Users/dino/Desktop/RobotFramework/libs/utils.py
Library    Collections

*** Variables ***
${CSV_FILE_USER}        /Users/dino/Desktop/RobotFramework/data/users.csv
${YAML_USER}            /Users/dino/Desktop/RobotFramework/output/data_user.yaml 
@{KEYS}                  Username    Password    Email  

*** Test Cases ***
Create user
    Log To Console    Creating a new instance of the Customer class
    Read Csv File from path    ${CSV_FILE_USER}
    Verify data before write to yaml    ${CSV_FILE_USER}    @{KEYS}
    Check User exists    ${CSV_FILE_USER}    ${YAML_USER}    @{KEYS}
    Create Data From Csv    ${CSV_FILE_USER}    ${YAML_USER}    @{KEYS}
    Verify data after write to yaml    ${YAML_USER}    @{KEYS}

*** Keywords ***
Read Csv File from path
    [Arguments]    ${file_path}
    Log To Console    Reading CSV file: ${file_path}
    ${data}=    Read Csv file    ${file_path}
    [Return]    ${data}

Verify data before write to yaml
    [Arguments]    ${file_path}    @{keys}
    ${data}=    Read Csv File   ${file_path}
    Log To Console    ['${keys[1]}']
    Check Username    ${data}    ['${keys[0]}']
    Check Password    ${data}   ['${keys[1]}']
    Check Email    ${data}    ['${keys[2]}']

Check User exists 
    [Arguments]    ${file_path}    ${yaml_file}    @{keys}
    Log To Console    Check user exists
    ${user} =     Read CSV file   ${file_path}
    FOR    ${row}    IN    @{user}
        ${user_exists} =    Check User Created   ${row}    ['${keys[0]}']    ${yaml_file}
        Run Keyword If    ${user_exists}    Log    User ${row['${keys[0]}']} already exists
    END    

Create data from CSV 
    [Arguments]    ${file_path}    ${yaml_file}    @{keys}
    Log To Console    Create user from CSV
    ${user} =     Read CSV file   ${file_path}
    FOR    ${row}    IN    @{user}
        ${user_exists} =    Check User exists    ${file_path}    ${yaml_file}    ['${keys[0]}']    
        Run Keyword If    not ${user_exists}    Create Data From Csv  ${row}    ${yaml_file}    ['${keys[0]}']
    END   

Verify data after write to yaml
    [Arguments]    ${yaml_file}    @{keys}
    Log To Console    Verifying data after write to yaml
    @{data} =    Read YAML file   ${yaml_file}
    Check Username     @{data}    ['${keys[0]}']
    Check Email    @{data}    ['${keys[1]}']
    Check Password @{data}    ['${keys[2]}']

    
 





