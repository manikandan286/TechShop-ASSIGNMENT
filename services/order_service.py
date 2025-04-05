from database.db_connector import get_connection
from models.orders import Order
from models.order_details import OrderDetails

class OrderService:
    @staticmethod
    def place_order(customer_id, product_id, quantity):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (%s, NOW())", (customer_id,))
        order_id = cursor.lastrowid
        cursor.execute("INSERT INTO order_details (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                       (order_id, product_id, quantity))
        connection.commit()
        connection.close()
        return OrderDetails(order_id, product_id, quantity)
