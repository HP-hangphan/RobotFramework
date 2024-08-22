import utils
import sys

sys.path.insert(0, "/Users/dino/Desktop/RobotFramework/data")

from properties import required_fields_customer, required_fields_user

# from save_to_yaml import write_to_file

file = "../data/Customer.csv"
file1 = "../data/users.csv"
yaml_customer = "../output/data_customer.yaml"
yaml_user = "../output/data_user.yaml"

user = utils.read_csv_file(file1)
customer = utils.read_csv_file(file)


new_user_data = {
    "FirstName": "John",
    "LastName": "Doe",
    "Email": "john.doe@example.com",
    "Phone": "0987654321",
}

utils.check_name(customer, ["FirstName", "LastName"])
# utils.check_phone_number(customer, ["Phone"])
utils.check_email(customer, ["Email"])
# utils.check_username(user, ["Username"])
# utils.check_password(user, ["Password"])
# utils.check_properties(customer, required_fields_customer)

# clea
# utils.check_user_created("John", yaml_file)
# utils.check_user_created({"FirstName": "Hi"}, ["FirstName"], yaml_file)
utils.create_data_from_csv(file, yaml_customer, ["FirstName"])

# utils.create_user_from_csv(file, yaml_customer, ["FirstName"])
