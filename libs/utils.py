import re
import yaml
import csv
from typing import Union


def read_csv_file(file_path):
    with open(file_path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        customers = [row for row in reader]
        return customers


def read_yaml_file(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        return yaml.safe_load(file) or []


def write_file(data, file_yaml):
    with open(file_yaml, mode="w", encoding="utf-8") as file:
        yaml.dump(data, file, default_flow_style=False)


def pattern_name(name: str):
    name_pattern = re.compile(r"^[A-Za-z]+$")
    assert name_pattern.match(name)


def check_name(data: Union[list, dict], keys: list):
    if isinstance(data, dict):
        for key in keys:
            pattern_name(data.get(key))
    elif isinstance(data, list):
        for row in data:
            check_name(row, keys)


def check_username(data: Union[list, dict], keys: list):
    username_pattern = re.compile(r"^[a-zA-Z0-9_]{3,15}$")
    if isinstance(data, dict):
        for key in keys:
            assert username_pattern.match(data.get(key))
    elif isinstance(data, list):
        for row in data:
            check_username(row, keys)


def check_email(data: Union[list, dict], keys: list):
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if isinstance(data, dict):
        for key in keys:
            assert email_pattern.match(data.get(key))
    elif isinstance(data, list):
        for row in data:
            check_email(row, keys)


def check_password(data: Union[list, dict], keys: list[str]):
    password_pattern = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
    if isinstance(data, dict):
        for key in keys:
            assert password_pattern.match(data.get(key))
    elif isinstance(data, list):
        for row in data:
            check_password(row, keys)


def check_phone_number(data: Union[list, dict], keys: list):
    pattern = re.compile(r"^(0|\+84)(3[2-9]|5[6|8|9]|7[0|6-9]|8[1-5]|9[0-9])[0-9]{7}$")
    if isinstance(data, dict):
        for key in keys:
            assert pattern.match(data.get(key))
    elif isinstance(data, list):
        for row in data:
            check_phone_number(row, keys)


def check_properties(data: Union[list, dict], required_key: list[str]):
    if isinstance(data, dict):
        for key in required_key:
            if not data.get(key):
                raise ValueError(f"Missing value for {key} in customer data")
    elif isinstance(data, list):
        for item in data:
            check_properties(item, required_key)


def check_user_created(data: Union[dict, list], keys: list, yaml_file) -> bool:
    try:
        users = read_yaml_file(yaml_file)
    except FileNotFoundError:
        return False

    if not isinstance(users, list):
        raise ValueError("Existing data in YAML file is not a list.")

    for user in users:
        if isinstance(user, dict) and all(
            user.get(key) == data.get(key) for key in keys
        ):
            print(f"User with {', '.join(keys)} already exists.")
            return True
    return False


def create_data_from_csv(csv_file, yaml_file, keys: list):
    new_users = []
    reader = read_csv_file(csv_file)
    for row in reader:
        if not check_user_created(row, keys, yaml_file):
            new_users.append(row)
        else:
            print(f"User already exists. Skipping creation.")
    if new_users:
        try:
            existing_users = read_yaml_file(yaml_file)
        except FileNotFoundError:
            existing_users = []
            write_file(existing_users + new_users, yaml_file)
            print("New users created successfully.")
    else:
        print("No new users to create.")
