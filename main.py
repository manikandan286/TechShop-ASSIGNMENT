from services.customer_service import CustomerService
from exceptions.custom_exceptions import CustomerNotFoundError

print("Fetching Customer Info:")
try:
    customer = CustomerService.get_customer(1)
    print("Customer Found:", customer)
except Exception as e:
    print("Error:", e)

print("\nUpdating Customer Info:")
try:
    # This update uses the same values, so you'll see "No changes detected..."
    CustomerService.update_customer(1, "john@example.com", "1234567890")
except Exception as e:
    print("Error:", e)

print("\nDeleting Customer Info:")
try:
    CustomerService.delete_customer(1)
except CustomerNotFoundError as e:
    print("Error:", e)
except Exception as e:
    print("Error:", e)
