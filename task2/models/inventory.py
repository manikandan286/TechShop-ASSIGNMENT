from datetime import datetime

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = datetime.now()

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        self.quantity_in_stock += quantity
        self.last_stock_update = datetime.now()

    def remove_from_inventory(self, quantity):
        if self.quantity_in_stock >= quantity:
            self.quantity_in_stock -= quantity
            self.last_stock_update = datetime.now()
        else:
            print("Not enough stock to remove!")

    def update_stock_quantity(self, new_quantity):
        self.quantity_in_stock = new_quantity
        self.last_stock_update = datetime.now()

    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.quantity_in_stock * self.product.price

    @staticmethod
    def list_low_stock_products(inventory_list, threshold):
        return [inv.product.product_name for inv in inventory_list if inv.quantity_in_stock < threshold]

    @staticmethod
    def list_out_of_stock_products(inventory_list):
        return [inv.product.product_name for inv in inventory_list if inv.quantity_in_stock == 0]

    @staticmethod
    def list_all_products(inventory_list):
        return [(inv.product.product_name, inv.quantity_in_stock) for inv in inventory_list]
