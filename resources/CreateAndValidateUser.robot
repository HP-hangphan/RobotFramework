*** Settings ***
Library     /Users/dino/Desktop/RobotFramework/libs/utils.py
Library     Collections


*** Variables ***
${CSV_FILE_USER}    /Users/dino/Desktop/RobotFramework/data/users.csv
${YAML_USER}        /Users/dino/Desktop/RobotFramework/output/data_user.yaml

@{KEYS}             Username    Password    Email
@{KEYS_CHECK}       Username    Email


*** Test Cases ***
Create user
    ${data} =    Read Csv File    ${CSV_FILE_USER}
    ${yaml_data} =    Read Yaml File    ${YAML_USER}
    Log To Console    Creating a new instance of the Customer class
    Verify data before write to yaml    ${data}    @{KEYS}
    Check User exists    ${CSV_FILE_USER}    ${YAML_USER}    @{KEYS_CHECK}
    Create Data From Csv    ${CSV_FILE_USER}    ${YAML_USER}    @{KEYS_CHECK}
    Verify data after write to yaml    ${yaml_data}    @{KEYS}


*** Keywords ***
Verify data before write to yaml
    [Arguments]    ${data}    @{keys}
    FOR    ${key}    IN    @{keys}
        Run Keyword    Check ${key} Field    ${data}    ${key}
    END

Check Username Field
    [Arguments]    ${data}    ${key}
    Check Username    ${data}    ${key}

Check Password Field
    [Arguments]    ${data}    ${key}
    Check Password    ${data}    ${key}

Check Email Field
    [Arguments]    ${data}    ${key}
    Check Email    ${data}    ${key}

Check User Exists
    [Arguments]    ${csv_file}    ${yaml_file}    @{keys_check}
    FOR    ${key}    IN    @{keys_check}
        Log To Console    Checking users for key: ${key}
        Run Keyword    Check ${key} User Created    ${csv_file}    ${yaml_file}    ${key}
    END

Check Username User Created
    [Arguments]    ${csv_file}    ${yaml_file}    ${key}
    ${user} =    Read Csv File    ${csv_file}
    FOR    ${row}    IN    @{user}
        ${value} =    Get From Dictionary    ${row}    ${key}
        ${user_exists} =    Check User Created    ${row}    ${key}    ${yaml_file}
        IF    ${user_exists}
            Log To Console    User with ${key} ${value} already exists
        END
    END

Check Email User Created
    [Arguments]    ${csv_file}    ${yaml_file}    ${key}
    ${user} =    Read Csv File    ${csv_file}
    FOR    ${row}    IN    @{user}
        ${value} =    Get From Dictionary    ${row}    ${key}
        ${user_exists} =    Check User Created    ${row}    ${key}    ${yaml_file}
        IF    ${user_exists}
            Log To Console    User with ${key} ${value} already exists
        END
    END

Create data from CSV
    [Arguments]    ${csv_file}    ${yaml_file}    @{keys_check}
    ${user} =    Read Csv File    ${csv_file}
    FOR    ${key}    IN    @{keys_check}
        Log To Console    Checking users for key: ${key}
        FOR    ${row}    IN    @{user}
            ${value} =    Get From Dictionary    ${row}    ${key}
            ${user_exists} =    Check User Created    ${row}    ${key}    ${yaml_file}
            IF    ${user_exists}
                Log To Console    User with ${key} ${value} already exists
            END
        END
        IF    not ${user_exists}
            Create Data From Csv    ${row}    ${key}    ${yaml_file}
        END
    END

Verify data after write to yaml
    [Arguments]    ${yaml_data}    @{keys}
    FOR    ${key}    IN    @{keys}
        Run Keyword    Check ${key} Yaml File    ${yaml_data}    ${key}
    END

Check Username Yaml File
    [Arguments]    ${yaml_data}    ${key}
    Check Username    ${yaml_data}    ${key}

Check Password Yaml File
    [Arguments]    ${yaml_data}    ${key}
    Check Password    ${yaml_data}    ${key}

Check Email Yaml File
    [Arguments]    ${yaml_data}    ${key}
    Check Email    ${yaml_data}    ${key}
