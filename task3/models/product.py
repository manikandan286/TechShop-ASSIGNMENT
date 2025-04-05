# models/product.py

class Product:
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.price = price  # Uses setter for validation

    # product_id property
    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        if isinstance(value, int) and value > 0:
            self.__product_id = value
        else:
            raise ValueError("Product ID must be a positive integer")

    # product_name property
    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        if value.strip():
            self.__product_name = value
        else:
            raise ValueError("Product name cannot be empty")

    # description property
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    # price property
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__price = value
        else:
            raise ValueError("Price must be a non-negative number")

    def get_product_details(self):
        return (f"Product ID: {self.product_id}, Name: {self.product_name}, "
                f"Description: {self.description}, Price: ₹{self.price:.2f}")

    def update_product_info(self, description=None, price=None):
        if description:
            self.description = description
        if price is not None:
            self.price = price

    def is_product_in_stock(self):
        return True  # Placeholder logic
