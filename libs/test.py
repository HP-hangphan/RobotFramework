from customer_data import read_csv_file

from utils import (
    validate_customer_name,
    check_username,
    check_email,
    check_phone_number,
    write_file,
    check_password,
    check_properties_user,
    # save_to_yaml,
)

# from save_to_yaml import write_to_file

file = "../data/Customer.csv"
file1 = "../data/users.csv"
yaml_file = "../output/data.yaml"

user = read_csv_file(file1)
customer = read_csv_file(file)


validate_customer_name(customer)
check_phone_number(customer)
check_email(customer)
check_username(user)
check_password(user)

write_file(user, yaml_file)

check_properties_user(user)


# write_to_file(file, yaml_file)
