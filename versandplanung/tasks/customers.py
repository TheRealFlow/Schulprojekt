import csv
from typing import List
from faker import Faker
import random
from os import path

fake = Faker()

cities: List[str] = ['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt', 'Stuttgart',
                     'Dusseldorf', 'Dortmund', 'Essen', 'Leipzig', 'Bremen', 'Dresden', 'Rostock']

num_customers = 150

customers = [{'UserId': fake.uuid4(), 'First_Name': fake.first_name(), 'Last_Name': fake.last_name(
), 'City': random.choice(cities), 'E-Mail': fake.email()} for _ in range(num_customers)]

csv_file_path = "../../datasources/customer_data.csv"
absolute_path = path.abspath(csv_file_path)

with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['UserId', 'First_Name', 'Last_Name', 'City', 'E-Mail']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customers)
