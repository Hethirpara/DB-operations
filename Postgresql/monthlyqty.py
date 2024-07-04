import psycopg2
import csv
from datetime import datetime

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
    
    cursor.execute("DELETE FROM sales_data")
    connection.commit()
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            date = datetime.strptime(row[0], '%Y-%m-%d').date()
            sku = row[1]
            unit_price = float(row[2])
            quantity = int(row[3])
            total_price = float(row[4])
            cursor.execute(
                "INSERT INTO sales_data (date, sku, unit_price, quantity, total_price) VALUES (%s, %s, %s, %s, %s)",
                (date, sku, unit_price, quantity, total_price)
            )
    
    connection.commit()
    print("Data inserted successfully!")
    
    query = '''
    SELECT
        to_char(date, 'YYYY-MM') AS month,
        sku,
        SUM(quantity) AS total_quantity
    FROM
        sales_data
    GROUP BY
        month, sku
    ORDER BY
        month, total_quantity DESC;
    '''
    cursor.execute(query)
    results = cursor.fetchall()

    popular_items = {}
    for row in results:
        month, sku, total_quantity = row
        if month not in popular_items:
            popular_items[month] = (sku, total_quantity)
    
    for month, (sku, total_quantity) in popular_items.items():
        print(f"Most popular item in {month}: {sku} with {total_quantity} units sold")
    
    cursor.close()
    connection.close()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
