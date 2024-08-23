import os

root_dir = os.path.dirname(__file__).replace("data", "")
DEFAULT_FILE_CSV_USER = os.path.join(root_dir, "data", "users.csv")
DEFAULT_FILE_CSV_CUSTOMER = os.path.join(root_dir, "data", "Customer.csv")
DEFAULT_FILE_YAML_USER = os.path.join(root_dir, "output", "data_user.yaml")
DEFAULT_FILE_YAML_CUSTOMER = os.path.join(root_dir, "output", "data_customer.yaml")

BASE_USER = {"Username": "", "Password": "", "Email": ""}
