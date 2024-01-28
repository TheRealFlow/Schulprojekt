from django.contrib import admin
from versandplanung.orders.models import Orders

class OrdersAdmin(admin.ModelAdmin):
    database = 'orders'
    list_display = ('id', 'orderNumber', 'customerId', 'articles', 'address')
    list_filter = ('id', 'orderNumber', 'customerId', 'articles', 'address')
    search_fields = ('id', 'orderNumber', 'customerId', 'articles', 'address')
    list_display_links = ('id',)
    
    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.database)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.database)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(OrdersAdmin, self).get_queryset(request).using(self.database)

admin.site.register(Orders, OrdersAdmin)
