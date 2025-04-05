# main.py

from models.product import Product

# Create a product
p = Product(1, "Laptop", "High performance laptop", 55000)

print(p.get_product_details())

# Try invalid price
try:
    p.price = -2000
except ValueError as e:
    print("Error:", e)

# Update info
p.update_product_info(description="2024 Model", price=60000)
print(p.get_product_details())
