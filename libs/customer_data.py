import csv

def read_csv_file(file_path):
    with open(file_path, mode='r') as f:
        reader = csv.DictReader(f)
        customers = []
        for row in reader:
            validate_customer_data(row)
            customers.append(row)
            print(row)
        return customers  
    
def validate_customer_data(customer_data):
    required_fields = ['FirstName', 'LastName', 'Phone', 'Email']
    for field in required_fields:
        if not customer_data.get(field):
            raise ValueError(f"Missing required field: {customer_data}")
        
        if "@" not in customer_data['Email']:
            raise ValueError(f"Invalid email format: {customer_data['Email']}")
        
        if len(customer_data['Phone']) != 10:
            raise ValueError(f"Invalid phone number format: {customer_data['Phone']}")
        
        if not customer_data['FirstName'].isalpha() or not customer_data['LastName'].isalpha():
            raise ValueError(f"Invalid first or last name format: {customer_data['FirstName']} {customer_data['LastName']}")
read_csv_file('../data/Customer.csv')