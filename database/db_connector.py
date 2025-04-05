
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mani",
        database="TechShopDB"  # 🔍 Check if this is correct!
    )
