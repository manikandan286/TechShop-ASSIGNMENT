class OrderDetail:
    def __init__(self, order_detail_id, order, product, inventory, quantity):
        self.order_detail_id = order_detail_id
        self.order = order
        self.product = product
        self.inventory = inventory
        self.quantity = quantity
        self.discount = 0.0
        order.order_details.append(self)
        inventory.remove_from_inventory(quantity)

    def calculate_subtotal(self):
        return self.quantity * self.product.price * (1 - self.discount)

    def get_order_detail_info(self):
        return f"{self.product.product_name}: Qty={self.quantity}, Subtotal=${self.calculate_subtotal():.2f}"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def add_discount(self, discount_percent):
        self.discount = discount_percent / 100
