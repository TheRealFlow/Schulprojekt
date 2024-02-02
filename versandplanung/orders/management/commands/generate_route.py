from json import dumps
from django.core.management.base import BaseCommand, CommandParser, CommandError
from requests import post
from versandplanung.orders.definitions import MAP_CITY_TO_WAREHOUSE_LOCATION
from versandplanung.orders.models import Orders

from versandplanung.vehicles.models import Vehicle

class Command(BaseCommand):
    help = 'Generates the delivery routes for the next day.'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--vehicle_count', type=int, help='The number of vehicles to use for the delivery routes.')
        parser.add_argument('--warehouse_location', type=str, help='The location (lng/lat) of the warehouse to use as the starting point for the delivery routes.')

    def handle(self, *args, **options):
        warehouse_location = (54.092225118165224, 12.140670094635173) # Rostock Office
        time_window = (0, 60*60*48) # 48 hours (in seconds)
        
        vehicle_count = options['vehicle_count']
        if vehicle_count is None or isinstance(vehicle_count, int) is False:
            vehicle_count = Vehicle.objects.count()
            
        if options['warehouse_location']:
            warehouse_location = tuple(map(float, options['warehouse_location'].split(',')))
        
        orders = Orders.objects.all()
        
        api_key = '71716aa4be0a4ba98c45aed9a7437379'
        request_url = 'https://api.geoapify.com/v1/routeplanner?apiKey=%s' % api_key
        headers = {'Content-Type': 'application/json'}
        data = {
            "mode": "drive",
            "agents": [{"start_location": [warehouse_location[1], warehouse_location[0]], "time_windows": [[time_window[0], time_window[1]]]} for _ in range(vehicle_count)],
            "shipments": [{
             "id": str(order.orderNumber),
             "pickup": {"location": [warehouse_location[1], warehouse_location[0]], "duration": 120},
             "delivery": {"location": MAP_CITY_TO_WAREHOUSE_LOCATION[order.address], "duration":120}
            } for order in orders ],
        }

        try:
            response = post(request_url, headers=headers, data=dumps(data))
            print(response.json())
            with open('delivery_routes.json', 'w') as file:
                file.write(dumps(response.json()))
                file.close()
        except Exception as error:
            raise CommandError("Couldn't generate delivery routes.", error) from error
        
