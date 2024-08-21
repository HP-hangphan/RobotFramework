import re
import yaml
from customer_data import read_csv_file


def validate_customer_name(data):
    for row in data:
        name_pattern = re.compile(r"^[\-'a-zA-Z ]+$")
        first_name = row.get("FirstName")
        last_name = row.get("LastName")
        if not name_pattern.match(first_name):
            raise Exception(f"Invalid FirstName: {first_name}")
        if not name_pattern.match(last_name):
            raise Exception(f"Invalid LastName: {last_name}")


def check_username(data):
    for row in data:
        username = row.get("Username")
        username_pattern = re.compile(r"^[a-zA-Z0-9_]{3,15}$")
        if not username_pattern.match(username):
            raise Exception(f"Invalid Username: {username}")


def check_email(data):
    for row in data:
        email = row.get("Email")
        email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        if not email_pattern.match(email):
            raise Exception(f"Invalid Email: {email}")


def check_password(data):
    for row in data:
        password = row.get("Password", "")
        password_pattern = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
        if not password_pattern.match(password):
            raise Exception(f"Invalid Password: {password}")


def check_phone_number(data):
    for row in data:
        phone_number = row.get("Phone")
        pattern = re.compile(
            r"^(0|\+84)(3[2-9]|5[6|8|9]|7[0|6-9]|8[1-5]|9[0-9])[0-9]{7}$"
        )
        if not pattern.match(phone_number):
            raise Exception(f"Invalid Phone Number: {phone_number}")


# def read_yaml_file(filename):
#     with open(filename, "r") as file:
#         return yaml.safe_load(file)


def write_file(data, file_yaml):
    with open(file_yaml, "w") as file:
        for row in data:
            yaml.dump(row, file, default_flow_style=False)
            print("file to dump")
        file.write("\n")


required_fields_customer = ["FirstName", "LastName", "Email", "Phone"]
required_fields_user = ["Username", "Password", "Email"]


def check_properties_customer(data):
    for field in required_fields_customer:
        for row in data:
            if not row.get(field):
                raise ValueError(f"Missing value for {field} in user data")


def validate_properties_user(data):
    for field in required_fields_user:
        for row in data:
            if not row.get(field):
                raise ValueError(f"Missing value for {field} in user data")
