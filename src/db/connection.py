import mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import MySQLConnectionPool
from contextlib import contextmanager
from src.config import Config

pool = None


def initialize_connection_pool():
    global pool
    try:
        pool = MySQLConnectionPool(
            pool_name="qubit_pool",
            pool_size=5,
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            database=Config.DB_NAME
        )
        print("Connection pool created successfully")
    except Error as err:
        print(f"Error creating connection pool: {err}")


@contextmanager
def get_db_connection():
    if pool is None:
        initialize_connection_pool()

    connection = None
    try:
        connection = pool.get_connection()
        yield connection
    except Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            connection.close()

# Usage example:
# with get_db_connection() as conn:
#     # Use the connection
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM your_table")
#     # Process results