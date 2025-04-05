# models/product.py

class Product:
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price

    def get_product_details(self):
        return f"Product [{self.__product_id}]: {self.__product_name}, ₹{self.__price:.2f} - {self.__description}"
