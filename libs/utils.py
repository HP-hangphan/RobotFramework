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
    return name_pattern.match(name)


def check_firstname(firstname):
    assert pattern_name(firstname)


def check_lastname(lastname):
    assert pattern_name(lastname)


def check_username(username: str):
    username_pattern = re.compile(r"^[a-zA-Z0-9_]{3,15}$")
    assert username_pattern.match(username)


def check_email(email: str):
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    assert email_pattern.match(email)


def check_password(password: str):
    password_pattern = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
    assert password_pattern.match(password)


def check_phone(phone):
    phone_pattern = re.compile(
        r"^(0|\+84)(3[2-9]|5[6|8|9]|7[0|6-9]|8[1-5]|9[0-9])[0-9]{7}$"
    )
    assert phone_pattern.match(phone)


def check_customer_information(customer: dict):
    if not config.BASE_CUSTOMER.keys() == customer.keys():
        raise Exception(
            "Input user [{}] doesn't match format with database".format(customer)
        )
    if is_user_exists(customer):
        logger.info("User [{}] already exists".format(customer), also_console=True)
        return False
    check_username(customer.get("FirstName"))
    check_password(customer.get("LastName"))
    check_phone(customer.get("Phone"))
    check_email(customer.get("Email"))
    return True


def is_customer_exists(customer: dict):
    customers = read_yaml_file(config.DEFAULT_FILE_YAML_CUSTOMER)
    if isinstance(customer, dict):
        is_exist = [
            customer
            for customer in customers
            if customer.get("Email") == customer.get("Email")
            or customer.get("Phone") == customer.get("Phone")
        ]
        if is_exist:
            return True


def is_customer_created(customer: Union[dict, list]) -> bool:
    customers = read_yaml_file(config.DEFAULT_FILE_YAML_CUSTOMER)
    if isinstance(customer, dict):
        return customer in customers
    elif isinstance(customer, list):
        for customer in customers:
            if customer not in customers:
                return False
        return True


def create_customer(customer: Union[list, dict]):
    customers = read_yaml_file(config.DEFAULT_FILE_YAML_CUSTOMER)
    if isinstance(customer, dict):
        if check_customer_information(customer):
            customers.append(customer)
            logger.info("User [{}] was created".format(customer), also_console=True)
    elif isinstance(customer, list):
        created = []
        for _customer in customer:
            if check_customer_information(_customer):
                created.append(_customer)
        if created:
            customers.extend(created)
            logger.info("Users [{}] were created".format(created), also_console=True)
    write_yaml(customers, config.DEFAULT_FILE_YAML_CUSTOMER)


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
