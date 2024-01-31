import pandas as pd
from faker import Faker
import random

fake = Faker()

num_articles = 100

articles = [{'ProduktID': i + 1, 'Produktname': fake.word() + ' ' + fake.word(),
             'Preis (€)': f"{round(random.uniform(10, 100), 2)} €"} for i in range(num_articles)]

excel_file_path = 'article_data.xlsx'

with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    articles_df = pd.DataFrame(articles)
    articles_df.to_excel(writer, sheet_name='Artikel', index=False)
