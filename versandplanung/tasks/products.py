from openpyxl import Workbook
import csv
import os
from faker import Faker

fake = Faker()

raw_data = "../../datasources/articles.csv"
absolute_path = os.path.abspath(raw_data)
print(absolute_path)

with open(absolute_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    wb = Workbook()
    ws = wb.active
    ws.append(["ProductId", "Price in Euro", "Article Name", "Short Description"])
    for row in csv_reader:
        ws.append([fake.uuid4(), fake.random_int(min=1, max=200), row["Name"], row["Description"]])

# Save the workbook to an Excel file
wb.save('../../datasources/articles.xlsx')

print("Mock articles data generated and saved to mock_articles.xlsx")
