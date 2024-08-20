from convert_to_dict import convert_to_dict
import re

def check_phone_number(customer_data: dict[str:str]):
    data = convert_to_dict(customer_data)
    phone_number = data.get('Phone', '')
    pattern = re.compile(r"^(0|\+84)(3[2-9]|5[6|8|9]|7[0|6-9]|8[1-5]|9[0-9])[0-9]{7}$")
    if pattern.match(phone_number):
        print("Phone number is valid", phone_number)
        
    else:
        print("Phone number is not valid")
        
