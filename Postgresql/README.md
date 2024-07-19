# Sales Data Analysis

## Project Description

This repository contains a set of Python scripts for managing and analyzing sales data using PostgreSQL. The project includes scripts for:
- Creating and populating a PostgreSQL table with sales data.
- Performing various analyses on the sales data, including calculating monthly sales, finding the most popular items, and summarizing revenue.

## Project Structure

The project consists of the following scripts:
- **`data_import.py`**: Creates the `sales_data` table and imports data from `sales-data.txt`.
- **`minmaxavg.py`**: Calculates and displays the minimum, maximum, and average quantity of sales per item per month.
- **`monthlyqty.py`**: Identifies and prints the most popular item per month based on total quantity sold.
- **`monthlysale.py`**: Calculates and displays the total sales amount per month.
- **`mostrev.py`**: Summarizes the total revenue per item per month.
- **`totalsales.py`**: Computes the total sales for the entire dataset.

## Setup

### Prerequisites

- Python 3.x
- PostgreSQL
- `psycopg2` library for PostgreSQL interaction

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sales-data-analysis.git
    ```

2. Change directory to the project folder:
    ```bash
    cd sales-data-analysis
    ```

3. Install the required Python packages:
    ```bash
    pip install psycopg2
    ```

4. Update `db_params` in each script with your PostgreSQL database credentials.

## Usage

1. Ensure PostgreSQL is running and your database is set up.

2. Place the `sales-data.txt` file in the appropriate directory (`D:/python/crud_app/`).

3. Run each script in the following order:

    - **Import data and create the table**:
      ```bash
      python data_import.py
      ```

    - **Perform analysis**:
      ```bash
      python minmaxavg.py
      python monthlyqty.py
      python monthlysale.py
      python mostrev.py
      python totalsales.py
      ```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Submit a pull request describing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [your-email@example.com](mailto:your-email@example.com).
