class Inventory:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def AddStock(self, qty):
        self.quantity += qty

    def RemoveStock(self, qty):
        if qty > self.quantity:
            raise Exception("Insufficient stock")
        self.quantity -= qty

    def __str__(self):
        return f"{self.product.ProductName} - Stock: {self.quantity}"
