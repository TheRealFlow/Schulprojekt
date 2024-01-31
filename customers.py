import csv
from faker import Faker
import random

fake = Faker()

cities = ['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt',
          'Stuttgart', 'Dusseldorf', 'Dortmund', 'Essen', 'Leipzig']

num_customers = 100

customers = [{'Vorname': fake.first_name(), 'Nachname': fake.last_name(
), 'Stadt': random.choice(cities), 'E-Mail': fake.email()} for _ in range(num_customers)]

orders = [{'Kundennummer': random.randint(1, num_customers), 'Produkt': fake.word(
), 'Menge': random.randint(1, 10), 'Preis': round(random.uniform(10, 100), 2)} for _ in range(200)]

csv_file_path = 'customer_data.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['Vorname', 'Nachname', 'Stadt', 'E-Mail']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customers)

excel_file_path = 'order_data.xlsx'

with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    customers_df = pd.DataFrame(customers)
    orders_df = pd.DataFrame(orders)

    orders_df['Kundennummer'] = orders_df['Kundennummer'].apply(
        lambda x: random.randint(1, num_customers))

    customers_df.to_excel(writer, sheet_name='Kunden', index=False)
    orders_df.to_excel(writer, sheet_name='Bestellungen', index=False)
