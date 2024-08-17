import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Construct the database connection URL
engine_url = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
print(f"Connecting to: mysql+pymysql://{os.getenv('DB_USER')}:****@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

try:
    # Create an SQLAlchemy engine
    engine = create_engine(engine_url)
    with engine.connect() as connection:
        print("Successfully connected to the database.")
except Exception as e:
    print(f"Error connecting to the database: {e}")