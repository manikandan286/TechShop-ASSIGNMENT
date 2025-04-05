from models.product import Product
from models.inventory import Inventory
from models.orders import Order

products = []
orders = []
inventory = {}

# Add Product
p1 = Product(101, "Keyboard", 500)
p2 = Product(102, "Mouse", 300)
products.append(p1)
products.append(p2)

# Add to Inventory
inventory[p1.ProductID] = Inventory(p1, 10)
inventory[p2.ProductID] = Inventory(p2, 5)

# Place an Order
o1 = Order(1, "Alice", p1, 2)
orders.append(o1)
inventory[p1.ProductID].RemoveStock(2)

# Search Product
search_name = "Mouse"
search_result = [p for p in products if search_name.lower() in p.ProductName.lower()]

# Sort Orders by Date
sorted_orders = sorted(orders, key=lambda x: x.order_date)

# Output
print("=== Products List ===")
for p in products:
    print(p)

print("\n=== Inventory Status ===")
for i in inventory.values():
    print(i)

print("\n=== Orders ===")
for o in sorted_orders:
    print(o)

print("\n=== Search Result ===")
for s in search_result:
    print(s)
