class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    @property
    def ProductID(self):
        return self.__product_id

    @property
    def ProductName(self):
        return self.__name

    @property
    def Price(self):
        return self.__price

    def __str__(self):
        return f"{self.__product_id} - {self.__name} - ₹{self.__price}"
