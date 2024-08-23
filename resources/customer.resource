*** Settings ***
Resource    ../tests/create_and_validate_customer_tests.robot


*** Keywords ***
Verify data before write to yaml
    [Arguments]    ${csv_file}    @{keys_customer}
    ${customer} =    Read Csv File    ${csv_file}
    FOR    ${key}    IN    @{keys_customer}
        Run Keyword    Check ${key}    ${customer}    ${key}
    END

Check Customer Exists
    [Arguments]    ${csv_file}    ${yaml_file}    @{keys}
    ${customer} =    Read Csv File    ${csv_file}
    FOR    ${key}    IN    @{keys}
        Log To Console    Checking customer for key: ${key}
        FOR    ${row}    IN    @{customer}
            Log To Console    ${row}
            Run Keyword    Check User Created    ${row}    ${yaml_file}    ${key}
        END
    END

Verify data after write to yaml
    [Arguments]    ${yaml_data}    @{keys_customer}
    FOR    ${key}    IN    @{keys_customer}
        Run Keyword    Check ${key}    ${yaml_data}    ${key}
    END

Create data Customer from CSV
    [Arguments]    ${csv_file}    ${yaml_file}    @{keys}
    ${customer} =    Read Csv File    ${csv_file}
    FOR    ${key}    IN    @{keys}
        Log To Console    Checking customer for key: ${key}
        FOR    ${row}    IN    @{customer}
            ${value} =    Get From Dictionary    ${row}    ${key}
            ${user_exists} =    Check User Created    ${row}    ${yaml_file}    ${key}
            IF    ${user_exists}
                Log To Console    Customer with ${key} ${value} already exists
            END
        END
        IF    not ${user_exists}
            Verify data before write to yaml    ${csv_file}    ${key}
            Create Data From Csv    ${csv_file}    ${yaml_file}    ${key}
            ${yaml_data} =    Read Yaml File    ${yaml_file}
            Verify data after write to yaml    ${yaml_data}    ${key}
        END
    END
