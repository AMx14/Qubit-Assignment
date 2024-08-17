import mysql.connector
from mysql.connector import Error
from src.config import Config

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            database=Config.DB_NAME
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except Error as err:
        print(f"Error: {err}")
        return None
