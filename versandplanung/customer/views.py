from django.shortcuts import render

import csv
from os import path

from versandplanung.customer.models import Customer
from versandplanung.settings import BASE_DIR


def view_customers(request):
    customers = []
    csv_customer_path = "datasources/customer_data.csv"
    absolute_path = path.join(BASE_DIR, csv_customer_path)

    with open(absolute_path, newline='', encoding='UTF-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # \ufeffUserId is some random windows bullshit
            customers.append(Customer(row.get('\ufeffUserId', row.get('UserId')), row['First_Name'],
                             row['Last_Name'], row['City'], row['Street'], row['Street_Number'], row['E-Mail']))
    csv_file.close()

    return render(request, 'customers.html', {
        'customers': customers
    })
