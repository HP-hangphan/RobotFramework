*** Settings ***
Resource    ../resources/import.resource


*** Test Cases ***
Create customer
    ${data} =    Read Csv File    ${DEFAULT_FILE_CSV_CUSTOMER}
    Create Customer    ${data}
    ${created} =    Is Customer Created    ${data}
    Should Be True    ${created}
