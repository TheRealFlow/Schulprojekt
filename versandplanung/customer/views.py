from django.shortcuts import render

import csv
from os import path

from versandplanung.customer.models import Customer

def view_customers(request):
    customers = []
    csv_customer_path = "datasources/customer_data.csv"
    absolute_path = path.abspath(csv_customer_path)
    
    with open(absolute_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            customers.append(Customer(row['UserId'], row['First_Name'], row['Last_Name'], row['City'], row['E-Mail']))
    csv_file.close()

    return render(request, 'customers.html', {
        'customers': customers
    })
