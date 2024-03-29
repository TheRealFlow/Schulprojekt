from django.contrib import admin
from versandplanung.orders.models import Orders


class OrdersAdmin(admin.ModelAdmin):
    database = 'orders'
    list_display = ('id', 'orderNumber', 'customerId',
                    'articles', 'address', 'status', 'total')
    list_filter = ('id', 'orderNumber', 'customerId',
                   'articles', 'address', 'status', 'total')
    search_fields = ('id', 'orderNumber', 'customerId',
                     'articles', 'address', 'status', 'total')
    list_display_links = ('id',)

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'orders' database.
        obj.save(using=self.database)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'orders' database
        obj.delete(using=self.database)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'orders' database.
        return super(OrdersAdmin, self).get_queryset(request).using(self.database)


admin.site.register(Orders, OrdersAdmin)
