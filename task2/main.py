from models.customer import Customer
from models.product import Product
from models.inventory import Inventory
from models.order import Order
from models.order_detail import OrderDetail

# Create customer
cust = Customer(1, "Alice", "Smith", "alice@example.com", "9876543210", "123 Main St")

# Create product and inventory
prod = Product(101, "Smart Watch", "Fitness tracking watch", 199.99)
inv = Inventory(1, prod, 10)

# Create order
order = Order(1, cust)
detail = OrderDetail(1, order, prod, inv, 2)

# Calculate total
order.calculate_total_amount()

# Display output
print("=== CUSTOMER DETAILS ===")
print(cust.get_customer_details())

print("\n=== PRODUCT DETAILS ===")
print(prod.get_product_details())

print("\n=== ORDER DETAILS ===")
print(order.get_order_details())

print("\n=== INVENTORY LEFT ===")
print(f"{prod.product_name} remaining stock: {inv.get_quantity_in_stock()}")
