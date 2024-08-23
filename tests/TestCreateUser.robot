*** Settings ***
Resource    ../resources/import.resource

*** Test Cases ***
Create user
    ${data} =    Read Csv File    ${DEFAULT_FILE_CSV_USER}
    Create User    ${data}
    ${created}=    Is User Created    ${data}
    Should Be True    ${created}
