from datetime import datetime

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.order_date = datetime.now()
        self.total_amount = 0.0
        self.status = "Processing"
        self.order_details = []
        customer.orders.append(self)

    def calculate_total_amount(self):
        self.total_amount = sum([detail.calculate_subtotal() for detail in self.order_details])
        return self.total_amount

    def get_order_details(self):
        details = "\n".join([detail.get_order_detail_info() for detail in self.order_details])
        return (f"Order ID: {self.order_id}\nDate: {self.order_date}\n"
                f"Status: {self.status}\nTotal: ${self.total_amount:.2f}\nDetails:\n{details}")

    def update_order_status(self, new_status):
        self.status = new_status

    def cancel_order(self):
        self.status = "Cancelled"
        for detail in self.order_details:
            detail.inventory.add_to_inventory(detail.quantity)
