import psycopg2
import csv

db_params = {
    'dbname': 'quotes_db',
    'user': 'quotes_user',
    'password': 'quotesuser_password',
    'host': 'localhost', 
    'port': '5432'
}

file_path = 'D:/python/crud_app/sales-data.txt'

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS sales_data (
        date DATE,
        sku VARCHAR(50),
        unit_price NUMERIC,
        quantity INTEGER,
        total_price NUMERIC
    );
    '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully!")
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            cursor.execute(
                "INSERT INTO sales_data (date, sku, unit_price, quantity, total_price) VALUES (%s, %s, %s, %s, %s)",
                row
            )
    
    connection.commit()
    print("Data inserted successfully!")
    
    cursor.execute("SELECT SUM(total_price) FROM sales_data")
    total_sales = cursor.fetchone()[0]
    print(f"Total sales of the store: {total_sales}")
    
    cursor.close()
    connection.close()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
