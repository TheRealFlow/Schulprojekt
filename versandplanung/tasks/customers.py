import csv
from typing import List
from faker import Faker
import random
from os import path

fake = Faker()

# Liste von Städten und ihren zugehörigen Straßen
city_streets_mapping = {
    'Berlin': ['Alexanderplatz', 'Kurfürstendamm', 'Friedrichstraße', 'Unter den Linden'],
    'Hamburg': ['Reeperbahn', 'Mönckebergstraße', 'Jungfernstieg', 'Hafenstraße'],
    'Munich': ['Marienplatz', 'Odeonsplatz', 'Leopoldstraße', 'Kaufingerstraße'],
    'Cologne': ['Domkloster', 'Hohe Straße', 'Schildergasse', 'Rheinuferstraße'],
    'Frankfurt': ['Römerberg', 'Zeil', 'Kaiserstraße', 'Fressgass'],
    'Stuttgart': ['Königstraße', 'Schlossplatz', 'Calwer Straße', 'Theodor-Heuss-Straße'],
    'Dusseldorf': ['Königsallee', 'Altstadt', 'Schadowstraße', 'Rheinpromenade'],
    'Dortmund': ['Westenhellweg', 'Kuckelke', 'Ostenhellweg', 'Kleppingstraße'],
    'Essen': ['Rüttenscheider Straße', 'Kettwiger Straße', 'Limbecker Platz', 'Burgplatz'],
    'Leipzig': ['Grimmaische Straße', 'Nikolaistraße', 'Karl-Liebknecht-Straße', 'Hauptbahnhofstraße'],
    'Bremen': ['Sögestraße', 'Knochenhauerstraße', 'Schlachte', 'Herdentorsteinweg'],
    'Dresden': ['Prager Straße', 'Königstraße', 'Webergasse', 'Altmarkt'],
    'Rostock': ['Kröpeliner Straße', 'Lange Straße', 'Universitätsplatz', 'Am Strom']
}

cities: List[str] = list(city_streets_mapping.keys())

num_customers = 150

customers = [{'UserId': random.randint(1, 184094848), 'First_Name': fake.first_name(), 'Last_Name': fake.last_name(),
              'City': city,
              'Street': fake.random_element(city_streets_mapping[city]),
              'Street_Number': random.randint(1, 25),
              'E-Mail': fake.email()} for _ in range(num_customers) for city in cities]

csv_file_path = "../../datasources/customer_data.csv"
absolute_path = path.abspath(csv_file_path)

with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['UserId', 'First_Name', 'Last_Name',
                  'City', 'Street', 'Street_Number', 'E-Mail']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customers)
