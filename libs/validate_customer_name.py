from convert_to_dict import convert_to_dict
import re

def validate_customer_name(customer_data: dict[str, str]) :
    data = convert_to_dict(customer_data)
    name_pattern = re.compile(r"^[\-'a-zA-Z ]+$")
    if not data['FirstName'] and not data['LastName']:
        print("First Name and Last Name cannot be empty")
   
    first_name = data.get('FirstName', '')
    last_name = data.get('LastName', '')

    if not name_pattern.match(first_name):
        print(f"Invalid FirstName: {first_name}")
    else:
        print(f"FirstName: {first_name} is valid")
        
    if not name_pattern.match(last_name):
        print(f"Invalid LastName: {last_name}")
    else:
        print(f"LastName: {last_name} is valid")
    
