from models.customer import Customer
from exceptions.invalid_data_exception import InvalidDataException
from exceptions.insufficient_stock_exception import InsufficientStockException
from exceptions.incomplete_order_exception import IncompleteOrderException
from exceptions.payment_failed_exception import PaymentFailedException
from exceptions.authentication_exception import AuthenticationException
from exceptions.authorization_exception import AuthorizationException
from exceptions.concurrency_exception import ConcurrencyException

# Simulate Customer Email Validation
try:
    print("Testing Invalid Email:")
    c1 = Customer(email="invalid-email")
except InvalidDataException as e:
    print("Error:", e)

# Simulate Inventory Stock Error
try:
    print("\nTesting Inventory Stock Check:")
    class Inventory:
        def __init__(self, stock):
            self.QuantityInStock = stock

        def remove_from_inventory(self, quantity):
            if quantity > self.QuantityInStock:
                raise InsufficientStockException("Not enough stock for order!")
            self.QuantityInStock -= quantity

    inventory = Inventory(stock=5)
    inventory.remove_from_inventory(quantity=10)
except InsufficientStockException as e:
    print("Error:", e)

# Simulate Incomplete Order
try:
    print("\nTesting Incomplete Order:")
    class OrderDetail:
        def __init__(self, product=None):
            self._product = product

        def validate(self):
            if not self._product:
                raise IncompleteOrderException("Product is missing in order detail.")

    order_detail = OrderDetail()
    order_detail.validate()
except IncompleteOrderException as e:
    print("Error:", e)

# Simulate Payment Failure
try:
    print("\nTesting Payment Failure:")
    raise PaymentFailedException("Card declined.")
except PaymentFailedException as e:
    print("Error:", e)

# Simulate Authentication Error
try:
    print("\nTesting Authentication:")
    raise AuthenticationException("Login required.")
except AuthenticationException as e:
    print("Error:", e)

# Simulate Authorization Error
try:
    print("\nTesting Authorization:")
    raise AuthorizationException("Access denied.")
except AuthorizationException as e:
    print("Error:", e)

# Simulate Concurrency Error
try:
    print("\nTesting Concurrency Issue:")
    raise ConcurrencyException("Simultaneous update detected.")
except ConcurrencyException as e:
    print("Error:", e)

# Simulate File I/O Error
try:
    print("\nTesting File Logging:")
    with open("readonlyfile.txt", "r") as file:  # Replace with a read-only path to test
        file.write("Testing...")
except IOError as e:
    print("Error:", e)
