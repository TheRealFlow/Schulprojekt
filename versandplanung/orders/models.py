from django.db import models

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    orderNumber = models.UUIDField()
    customerId = models.IntegerField() # Foreign Key to Customer from xlsx file
    articles = models.JSONField() # JSON Array of articles (name and count) since the articles are present in a csv file
    address = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Orders" # on default django would display the name as "Orderss"