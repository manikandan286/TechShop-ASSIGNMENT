class ProductNotFoundError(Exception):
    def __init__(self, message="Product not found"):
        self.message = message
        super().__init__(self.message)

class InsufficientStockError(Exception):
    def __init__(self, message="Insufficient stock"):
        self.message = message
        super().__init__(self.message)

class CustomerNotFoundError(Exception):
    def __init__(self, message="Customer not found"):
        self.message = message
        super().__init__(self.message)
