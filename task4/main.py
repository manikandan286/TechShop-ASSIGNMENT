# main.py

from models.customer import Customer
from models.product import Product
from models.order import Order
from models.order_detail import OrderDetail

# Create Customer and Product
customer = Customer(101, "Arun", "Kumar", "arun@example.com", "9876543210", "Chennai")
product1 = Product(1, "Smartphone", "5G Android", 15000)
product2 = Product(2, "Laptop", "Core i7", 60000)

# Create Order
order = Order(1001, customer)

# Create OrderDetails
detail1 = OrderDetail(201, order, product1, 2)
detail2 = OrderDetail(202, order, product2, 1)

# Add OrderDetails to Order
order.add_order_detail(detail1)
order.add_order_detail(detail2)

# Calculate Total
order.calculate_total_amount()

# Print full order info
print(order.get_order_details())
