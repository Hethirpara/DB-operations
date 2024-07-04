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

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            date_str = row[0]
            date = datetime.strptime(date_str, '%Y-%m-%d').date()

            cursor.execute(
                "INSERT INTO sales_data (date, sku, unit_price, quantity, total_price) VALUES (%s, %s, %s, %s, %s)",
                (date, row[1], row[2], row[3], row[4])
            )

    connection.commit()
    print("Data inserted successfully!")

    cursor.execute("""
        SELECT DISTINCT ON (month)
               DATE_TRUNC('month', date) AS month,
               sku,
               MIN(quantity) AS min_orders,
               MAX(quantity) AS max_orders,
               AVG(quantity) AS avg_orders
        FROM sales_data
        GROUP BY month, sku
        ORDER BY month, COUNT(*) DESC
    """)

    results = cursor.fetchall()

    print("\nResults:")
    print("Month\t\tItem\t\tMin Orders\tMax Orders\tAvg Orders")
    for row in results:
        month = row[0].strftime('%Y-%m')
        sku = row[1]
        min_orders = row[2]
        max_orders = row[3]
        avg_orders = row[4]
        print(f"{month}\t{sku}\t\t{min_orders}\t\t{max_orders}\t\t{avg_orders:.2f}")

    cursor.close()
    connection.close()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL or executing queries:", error)
