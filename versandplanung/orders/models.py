from django.db import models


class OrdersManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('orders')


class Orders(models.Model):
    STATUS_CHOICES = (
        ('open', 'Offen'),
        ('in progress', 'In Bearbeitung'),
        ('shipped', 'Versendet'),
        ('delivered', 'Zugestellt'),
    )

    id = models.AutoField(primary_key=True)
    orderNumber = models.UUIDField()
    customerId = models.IntegerField()  # Foreign Key to Customer from xlsx file
    # JSON Array of articles (name and count) since the articles are present in a csv file
    articles = models.JSONField()
    address = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='open')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # doing this allows to call Orders.objects.all() instead of Orders.objects.using('orders').all()
    objects = OrdersManger()

    class Meta:
        # on default django would display the name as "Orderss"
        verbose_name_plural = "Orders"
