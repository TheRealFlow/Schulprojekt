from django.db import models

class OrdersManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('orders')

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    orderNumber = models.UUIDField()
    customerId = models.IntegerField() # Foreign Key to Customer from xlsx file
    articles = models.JSONField() # JSON Array of articles (name and count) since the articles are present in a csv file
    address = models.CharField(max_length=100)
    
    objects = OrdersManger() # doing this allows to call Orders.objects.all() instead of Orders.objects.using('orders').all()
    
    class Meta:
        verbose_name_plural = "Orders" # on default django would display the name as "Orderss"