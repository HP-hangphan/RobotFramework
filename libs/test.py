import utils
import sys
import os
import yaml

sys.path.insert(0, os.path.join(os.getcwd(), "data"))
import config
from properties import required_fields_customer, required_fields_user

file1 = config.DEFAULT_FILE_CSV_USER
file = config.DEFAULT_FILE_CSV_CUSTOMER

user = utils.read_csv_file(file1)
customer = utils.read_csv_file(file)
print(customer)


print(user)

new_user_data = {
    "FirstName": "John",
    "LastName": "Doe",
    "Email": "john.doe@example.com",
    "Phone": "0987654321",
}

# utils.check_name(customer, "FirstName")
# utils.check_phone_number(customer, ["Phone"])
# utils.check_email(user, "Email")
# utils.check_username(user, ["Username"])
# utils.check_password(user, ["Password"])
# utils.check_properties(customer, required_fields_customer)

# clea
# utils.check_user_created(new_user_data, "Username", yaml_user)

# utils.create_data_from_csv(file, yaml_customer, ["FirstName"])

# utils.create_user_from_csv(file, yaml_customer, ["FirstName"])
