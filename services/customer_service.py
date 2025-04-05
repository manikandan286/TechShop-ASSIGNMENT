from database.db_connector import get_connection
from exceptions.custom_exceptions import CustomerNotFoundError


class CustomerService:

    @staticmethod
    def get_customer(customer_id):
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM customers WHERE CustomerID = %s"
        print(f"Executing Query: {query} with ID: {customer_id}")
        cursor.execute(query, (customer_id,))
        customer = cursor.fetchone()
        print("Raw Query Result:", customer)
        connection.close()

        if not customer:
            print("Customer not found in database!")
            raise CustomerNotFoundError("Customer not found")

        return customer

    @staticmethod
    def update_customer(customer_id, new_email, new_phone):
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE customers SET Email = %s, Phone = %s WHERE CustomerID = %s"
        print(f"Executing Update: {query}")
        cursor.execute(query, (new_email, new_phone, customer_id))
        connection.commit()

        if cursor.rowcount == 0:
            # Check if the customer exists
            cursor.execute("SELECT * FROM customers WHERE CustomerID = %s", (customer_id,))
            result = cursor.fetchone()
            if result:
                print("No changes detected; update not necessary.")
                connection.close()
                return True
            else:
                connection.close()
                raise CustomerNotFoundError("Customer not found for update")

        print("Customer updated successfully.")
        connection.close()
        return True

    @staticmethod
    def delete_customer(customer_id):
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM customers WHERE CustomerID = %s"
        print(f"Executing Delete: {query} with ID: {customer_id}")
        cursor.execute(query, (customer_id,))
        connection.commit()

        if cursor.rowcount == 0:
            connection.close()
            raise CustomerNotFoundError("Customer not found for deletion")
        else:
            print("Customer deleted successfully.")

        connection.close()
        return True
