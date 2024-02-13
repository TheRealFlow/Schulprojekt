class Article:
    def __init__(self, id: str, name: str, price: int, short_description: str):
        self._id = id
        self._name = name
        self._price = price
        self._short_description = short_description

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_price(self) -> float:
        return self._price * 1.19  # add 19% VAT

    def get_short_description(self) -> str:
        return self._short_description[:46] + ' ...'
