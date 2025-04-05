from database.db_connector import get_connection
from models.inventory import Inventory
from exceptions.custom_exceptions import ProductNotFoundError

class InventoryService:
    @staticmethod
    def get_stock(product_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM inventory WHERE product_id = %s", (product_id,))
        row = cursor.fetchone()
        connection.close()

        if row:
            return Inventory(*row)
        else:
            raise ProductNotFoundError()
