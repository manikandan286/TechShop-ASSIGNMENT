from database.db_connector import get_connection
from models.products import Product
from exceptions.custom_exceptions import ProductNotFoundError

class ProductService:
    @staticmethod
    def get_product(product_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
        row = cursor.fetchone()
        connection.close()

        if row:
            return Product(*row)
        else:
            raise ProductNotFoundError()
