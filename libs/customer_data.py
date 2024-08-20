import csv

from convert_to_dict import convert_to_dict
from validate_customer_name import validate_customer_name
from check_phone_number import check_phone_number
from check_email import check_email

def read_csv_file(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter= "\t")
        customers = {}
        for index, row in enumerate(reader): 
                validate_customer_name(row)
                check_phone_number(row)
                check_email(row)
                
                customers[index] = row
                print(type(row))
                
        print(type(convert_to_dict(row)))
        return customers  
    
       




    

read_csv_file('../data/Customer.csv')
