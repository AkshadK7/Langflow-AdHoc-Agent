import sqlite3
import pandas as pd

def create_database(db_path, csv_path, table_name):
    """
    Creates a SQLite database, creates a table, and inserts CSV data into the table.
    
    :param db_path: Path to the SQLite database file
    :param csv_path: Path to the CSV file to be imported
    :param table_name: Name of the table to create
    """
    try:
        # Connect to SQLite database (or create it)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_path)

        # Create a table schema dynamically based on the CSV structure
        columns = ', '.join([f"'{col}' TEXT" for col in df.columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        cursor.execute(create_table_query)

        # Insert data into the table
        df.to_sql(table_name, conn, if_exists='append', index=False)
        conn.commit()
        conn.close()

        print(f"Database created successfully at {db_path} with table '{table_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify paths and table name
db_path = "./user_db.sqlite"  # Path to SQLite database
csv_path = "./data/user_data.csv"  # Path to your CSV file
table_name = "user_data"  # Name of the table

# Create database and insert data
create_database(db_path, csv_path, table_name)
