*** Settings ***
Resource    ../testsuite/test_suite_CreateAndValidateUser.robot


*** Keywords ***
Verify data before write to yaml
    [Arguments]    ${data}    @{keys}
    FOR    ${key}    IN    @{keys}
        Run Keyword    Check ${key}    ${data}    ${key}
    END

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

Verify data after write to yaml
    [Arguments]    ${yaml_data}    @{keys}
    FOR    ${key}    IN    @{keys}
        Run Keyword    Check ${key}    ${yaml_data}    ${key}
    END

Create data user from CSV
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
            Verify data before write to yaml    ${user}    ${key}
            Create Data From Csv    ${csv_file}    ${key}    ${yaml_file}
            ${yaml_data} =    Read Yaml File    ${yaml_file}
            Verify data after write to yaml    ${yaml_data}    ${key}
        END
    END
