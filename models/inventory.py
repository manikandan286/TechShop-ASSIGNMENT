class Inventory:
    def __init__(self, product_id, stock_quantity):
        self.product_id = product_id
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Inventory(Product ID: {self.product_id}, Stock: {self.stock_quantity})"
