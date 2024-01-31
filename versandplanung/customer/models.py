from versandplanung.customer.definitions import CITY_ZIP_CODE_MAP

class Customer:
    def __init__(self, id: str, first_name: str, last_name: str, city: str, email: str):
        self._id = id
        self._firstName = first_name
        self._last_name = last_name
        self._email = email
        self._city = city

    def get_id(self) -> str:
        return self._id

    def get_first_name(self) -> str:
        return self._firstName

    def get_last_name(self) -> str:
        return self._last_name
    
    def get_full_name(self) -> str:
        # capitalize last name to make it easier to read
        return self._firstName + " " + self._last_name.upper()

    def get_email(self) -> str:
        return self._email

    def get_city(self) -> str:
        return "%s %s" % (CITY_ZIP_CODE_MAP.get(self._city, '00000'), self._city )
        
    