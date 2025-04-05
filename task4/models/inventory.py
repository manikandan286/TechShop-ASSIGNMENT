# models/inventory.py

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock):
        self.__inventory_id = inventory_id
        self.__product = product  # Composition with Product
        self.__quantity_in_stock = quantity_in_stock

    def get_product(self):
        return self.__product

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def get_inventory_value(self):
        return self.__quantity_in_stock * self.__product._Product__price
