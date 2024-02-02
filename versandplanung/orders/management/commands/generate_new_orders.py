import csv
from typing import List
from django.core.management.base import BaseCommand, CommandError
from openpyxl import load_workbook
from os import path
from json import dumps
from faker import Faker
from versandplanung.articles.helpers import get_random_selection_from_list

from versandplanung.articles.models import Article
from versandplanung.customer.models import Customer
from versandplanung.orders.models import Orders
from versandplanung.vehicles.models import Vehicle


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        customer_data: List[Customer] = []
        try:
            file_path = path.abspath('datasources/customer_data.csv')
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    customer_data.append(Customer(row["UserId"], row["First_Name"], row["Last_Name"], row["City"], row["E-Mail"]))
            csv_file.close()
        except FileNotFoundError as error:
            raise CommandError("Couldn't find customer_data.csv file.", error)
        
        article_data: List[Article] = []
        try:
            articles_workbook = load_workbook('datasources/articles.xlsx')
            article_sheet = articles_workbook.active
            
            for row in article_sheet.iter_rows(min_row=1, max_row=article_sheet.max_row, values_only=True):
                article_data.append(Article(id=row[0], price=row[1], name=row[2], short_description=row[3]))

            articles_workbook.close()
        except FileNotFoundError:
            raise CommandError("Couldn't find articles.xlsx file.")

        Orders.objects.all().delete()
        for user in customer_data:
            Orders.objects.create(orderNumber=fake.uuid4(), customerId=user.get_id(), articles=get_random_selection_from_list(article_data), address=user.get_city())
        
        
        
        # vehicles_count = Vehicle.objects.count()