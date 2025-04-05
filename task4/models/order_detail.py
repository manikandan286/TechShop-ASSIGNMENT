# models/order_detail.py

class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order  # Composition with Order
        self.__product = product  # Composition with Product
        self.__quantity = quantity
        self.__discount = 0

    def calculate_subtotal(self):
        price = self.__product._Product__price  # Access private price
        subtotal = price * self.__quantity
        return subtotal * (1 - self.__discount)

    def get_order_detail_info(self):
        return f"Product: {self.__product.get_product_details()}, Quantity: {self.__quantity}, Subtotal: ₹{self.calculate_subtotal():.2f}"

    def add_discount(self, discount_percent):
        self.__discount = discount_percent / 100
