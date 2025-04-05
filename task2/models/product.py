class Product:
    def __init__(self, product_id, product_name, description, price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.in_stock = True

    def get_product_details(self):
        return (f"Product ID: {self.product_id}, Name: {self.product_name}, "
                f"Description: {self.description}, Price: ${self.price:.2f}")

    def update_product_info(self, description=None, price=None):
        if description:
            self.description = description
        if price is not None:
            self.price = price

    def is_product_in_stock(self):
        return self.in_stock
