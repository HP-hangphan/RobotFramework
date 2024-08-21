*** Settings ***
Library    ../libs/customer_data.py
Library    ../libs/utils.py

*** Variables ***
${CSV_FILE_CUSTOMER}    /Users/dino/Desktop/RobotFramework/data/Customer.csv
${CSV_FILE_USER}        /Users/dino/Desktop/RobotFramework/data/users.csv
${YAML_FILE}            ../output/data.csv

*** Test Cases ***
Validate data customer and user
    ${data_customer}=     customer_data.Read CSV File     ${CSV_FILE_CUSTOMER}
    ${data_user}=    customer_data.Read CSV File     ${CSV_FILE_USER}
    Validate Customer Name    ${data_customer}
    Check Email   ${data_customer}
    Check Email    ${data_user}
    Check Username    ${data_user}
    Check Password    ${data_user}







