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
        next(reader)  

        for row in reader:
            cursor.execute(
                "INSERT INTO sales_data (date, sku, unit_price, quantity, total_price) VALUES (%s, %s, %s, %s, %s)",
                row
            )

    connection.commit()
    print("Data inserted successfully!")

    month_wise_sales_query = '''
    SELECT TO_CHAR(date, 'YYYY-MM') AS month, SUM(total_price) AS total_sales
    FROM sales_data
    GROUP BY TO_CHAR(date, 'YYYY-MM')
    ORDER BY month;
    '''
    cursor.execute(month_wise_sales_query)
    month_wise_sales = cursor.fetchall()

    print("Month-wise sales totals:")
    for row in month_wise_sales:
        print(f"Month: {row[0]}, Total Sales: {row[1]}")

    cursor.close()
    connection.close()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
