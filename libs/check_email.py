import re
from convert_to_dict import convert_to_dict

def check_email(customer_data :dict[str:str]):
    data = convert_to_dict(customer_data)
    required_fields = ['Email']
    missing_fields = [
        field for field in required_fields if field not in data or not data[field]]

    if not data['Email']:
        print("Email cannot be empty")
        return False
    
    email = data.get('Email')
    
    if missing_fields:
        print(f"Missing fields: {', '.join(missing_fields)}")
   
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if not email_pattern.match(email):
        print("Invalid email format")
    else:
        print('Email is valid')
    
    

    return True