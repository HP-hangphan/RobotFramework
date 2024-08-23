*** Settings ***
Resource    ../testsuite/test_suite_ValidateAndCreateCustomer.robot


*** Keywords ***
Verify data before write to yaml
    [Arguments]    ${data}    @{keys_customer}
    FOR    ${key}    IN    @{keys_customer}
        Run Keyword    Check ${key}    ${data}    ${key}
    END

Check Customer Exists
    [Arguments]    ${csv_file}    ${yaml_file}    @{keys_check_customer}
    FOR    ${key}    IN    @{keys_check_customer}
        Log To Console    Checking customer for key: ${key}
        Run Keyword    Check ${key} Customer Created    ${csv_file}    ${yaml_file}    ${key}
    END

Check Email Customer Created
    [Arguments]    ${csv_file}    ${yaml_file}    ${key_customer}
    ${user} =    Read Csv File    ${csv_file}
    FOR    ${row}    IN    @{user}
        ${value} =    Get From Dictionary    ${row}    ${key_customer}
        ${user_exists} =    Check User Created    ${row}    ${key_customer}    ${yaml_file}
        IF    ${user_exists}
            Log To Console    User with ${key_customer} ${value} already exists
        END
    END

Check PHONE Customer Created
    [Arguments]    ${csv_file}    ${yaml_file}    ${key_customer}
    ${user} =    Read Csv File    ${csv_file}
    FOR    ${row}    IN    @{user}
        ${value} =    Get From Dictionary    ${row}    ${key_customer}
        ${user_exists} =    Check User Created    ${row}    ${key_customer}    ${yaml_file}
        IF    ${user_exists}
            Log To Console    User with ${key_customer} ${value} already exists
        END
    END

Verify data after write to yaml
    [Arguments]    ${yaml_data}    @{keys_customer}
    FOR    ${key}    IN    @{keys_customer}
        Run Keyword    Check ${key}    ${yaml_data}    ${key}
    END

Create data Customer from CSV
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
            Create Data From Csv    ${csv_file}    ${yaml_file}    ${key}
            ${yaml_data} =    Read Yaml File    ${yaml_file}
            Verify data after write to yaml    ${yaml_data}    ${key}
        END
    END
