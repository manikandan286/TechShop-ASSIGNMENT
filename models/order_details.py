class OrderDetails:
    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __str__(self):
        return f"OrderDetails(Order: {self.order_id}, Product: {self.product_id}, Quantity: {self.quantity})"
