class Customer:
    def __init__(self, id: str, first_name: str, last_name: str, city: str, street: str, street_number: str, email: str):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._city = city
        self._street = street
        self._street_number = street_number
        self._email = email

    def get_id(self) -> str:
        return self._id

    def get_first_name(self) -> str:
        return self._first_name

    def get_last_name(self) -> str:
        return self._last_name

    def get_full_name(self) -> str:
        # capitalize last name to make it easier to read
        return self._first_name + " " + self._last_name.upper()

    def get_city(self) -> str:
        return self._city

    def get_street(self) -> str:
        return self._street

    def get_street_number(self) -> str:
        return self._street_number

    def get_email(self) -> str:
        return self._email
