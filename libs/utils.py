import re
import yaml
import csv
from typing import Union
import os
import sys
from robot.api import logger

dir_name = os.path.dirname(__file__).replace("libs", "")
if dir_name not in sys.path:
    sys.path.append(dir_name)

from data import config


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


def write_yaml(data, file_path):
    with open(file_path, mode="w", encoding="utf-8") as file:
        yaml.dump(data, file, default_flow_style=False)


def pattern_name(name: str):
    name_pattern = re.compile(r"^[A-Za-z]+$")
    assert name_pattern.match(name)


def check_firstname(data: Union[list, dict], key: str):
    if isinstance(data, dict):
        pattern_name(data.get(key))
    elif isinstance(data, list):
        for row in data:
            check_firstname(row, key)


def check_lastname(data: Union[list, dict], key: str):
    if isinstance(data, dict):
        pattern_name(data.get(key))
    elif isinstance(data, list):
        for row in data:
            check_lastname(row, key)


def check_username(username: str):
    username_pattern = re.compile(r"^[a-zA-Z0-9_]{3,15}$")
    assert username_pattern.match(username)


def check_email(email: str):
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    assert email_pattern.match(email)


def check_password(password: str):
    password_pattern = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
    assert password_pattern.match(password)


def check_phone(data: Union[list, dict], key: str):
    pattern = re.compile(r"^(0|\+84)(3[2-9]|5[6|8|9]|7[0|6-9]|8[1-5]|9[0-9])[0-9]{7}$")
    if isinstance(data, dict):
        assert pattern.match(data.get(key))
    elif isinstance(data, list):
        for row in data:
            check_phone(row, key)


def check_properties(data: Union[list, dict], required_key: list[str]):
    if isinstance(data, dict):
        for key in required_key:
            if not data.get(key):
                raise ValueError(f"Missing value for {key} in customer data")
    elif isinstance(data, list):
        for item in data:
            check_properties(item, required_key)


def is_user_exists(user: dict):
    users = read_yaml_file(config.DEFAULT_FILE_YAML_USER)
    if isinstance(user, dict):
        is_exist = [
            _user
            for _user in users
            if user.get("Username") == user.get("Username")
            or user.get("Email") == user.get("Email")
        ]
        if is_exist:
            return True


def is_user_created(user: Union[dict, list]) -> bool:
    users = read_yaml_file(config.DEFAULT_FILE_YAML_USER)
    if isinstance(user, dict):
        return user in users
    elif isinstance(user, list):
        for user in users:
            if user not in users:
                return False
        return True


def create_user(user: Union[list, dict]):
    users = read_yaml_file(config.DEFAULT_FILE_YAML_USER)
    if isinstance(user, dict):
        if check_user_information(user):
            users.append(user)
            logger.info("User [{}] was created".format(user), also_console=True)
    elif isinstance(user, list):
        created = []
        for _user in user:
            if check_user_information(_user):
                created.append(_user)
        if created:
            users.extend(created)
            logger.info("Users [{}] were created".format(created), also_console=True)
    write_yaml(users, config.DEFAULT_FILE_YAML_USER)


def check_user_information(user: dict):
    if not config.BASE_USER.keys() == user.keys():
        raise Exception(
            "Input user [{}] doesn't match format with database".format(user)
        )
    if is_user_exists(user):
        logger.info("User [{}] already exists".format(user), also_console=True)
        return False
    check_username(user.get("Username"))
    check_password(user.get("Password"))
    check_email(user.get("Email"))
    return True
