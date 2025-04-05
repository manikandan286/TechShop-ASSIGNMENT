class Order:
    def __init__(self, order_id, customer_id, order_date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date

    def __str__(self):
        return f"Order({self.order_id}, Customer: {self.customer_id}, Date: {self.order_date})"
