from django.contrib import admin
from versandplanung.vehicles.models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    database = 'vehicles'
    list_display = ('id', 'brandName', 'modelName', 'modelYear', 'initalRegistration', 'licensePlate')
    list_filter = ('id', 'brandName', 'modelName', 'modelYear', 'initalRegistration', 'licensePlate')
    search_fields = ('id', 'brandName', 'modelName', 'modelYear', 'initalRegistration', 'licensePlate')
    list_display_links = ('id',)
    
    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.database)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.database)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(VehicleAdmin, self).get_queryset(request).using(self.database)

admin.site.register(Vehicle, VehicleAdmin)
