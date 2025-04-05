from datetime import datetime

class Order:
    def __init__(self, order_id, customer_name, product, quantity):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product = product
        self.quantity = quantity
        self.order_date = datetime.now()
        self.status = "Placed"

    def __str__(self):
        return f"Order {self.order_id} | {self.customer_name} | {self.product.ProductName} x {self.quantity} | {self.status} | {self.order_date.strftime('%Y-%m-%d')}"
