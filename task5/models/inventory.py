from exceptions.insufficient_stock_exception import InsufficientStockException

class Inventory:
    def remove_from_inventory(self, quantity):
        if quantity > self.QuantityInStock:
            raise InsufficientStockException("Attempted to sell more than stock.")
        self.QuantityInStock -= quantity
