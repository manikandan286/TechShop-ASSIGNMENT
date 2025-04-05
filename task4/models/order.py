# models/order.py
from datetime import datetime

class Order:
    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer  # Composition with Customer class
        self.__order_date = datetime.now()
        self.__total_amount = 0
        self.__status = "Processing"
        self.__details = []

    @property
    def customer(self):
        return self.__customer

    def add_order_detail(self, order_detail):
        self.__details.append(order_detail)

    def calculate_total_amount(self):
        self.__total_amount = sum(detail.calculate_subtotal() for detail in self.__details)
        return self.__total_amount

    def get_order_details(self):
        details = "\n".join([detail.get_order_detail_info() for detail in self.__details])
        return f"Order ID: {self.__order_id}, Date: {self.__order_date}, Customer: {self.customer.get_customer_details()},\nDetails:\n{details},\nTotal: ₹{self.__total_amount:.2f}"
