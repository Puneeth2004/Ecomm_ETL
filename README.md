# E-commerce Order ETL Pipeline

A Python-based ETL pipeline for processing e-commerce order data.

## Project Overview

This project implements a complete ETL (Extract, Transform, Load) pipeline for processing e-commerce order data. The pipeline extracts data from CSV files, validates and transforms it, then loads it into a MySQL database.

## Project Structure

```
Ecom_order/
├── data/
│   ├── raw/                    # Raw CSV data files
│   │   ├── categories.csv
│   │   ├── customers.csv
│   │   ├── inventory.csv
│   │   ├── orders.csv
│   │   ├── order_items.csv
│   │   ├── payments.csv
│   │   ├── products.csv
│   │   ├── returns.csv
│   │   ├── reviews.csv
│   │   └── shipping.csv
│   ├── cleaned/               # Cleaned data (gitignored)
│   └── processed/             # Processed data (gitignored)
├── database/
│   ├── schema.sql             # Database schema
│   ├── queries.sql            # SQL queries
│   └── views.sql              # Database views
├── etl/
│   ├── extract.py             # Data extraction module
│   ├── transform.py           # Data transformation module
│   ├── load.py                # Data loading module
│   ├── validate.py            # Data validation module
│   ├── mapping.py             # Data mapping module
│   └── utils.py               # Utility functions
├── reports/                   # Data quality reports
├── config.py                  # Database configuration
├── main.py                    # Main pipeline entry point
├── profiling.py               # Data profiling module
├── test_connection.py         # Database connection test
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation

1. Clone the repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Update the database configuration in `config.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "ecomm_db",
    "port": 3306
}
```

## Usage

Run the ETL pipeline:

```bash
python main.py
```

Test database connection:

```bash
python test_connection.py
```

## Features

- **Data Extraction**: Read multiple CSV files with e-commerce data
- **Data Validation**: Validate data quality and integrity
- **Data Transformation**: Clean and transform raw data
- **Data Loading**: Load processed data into MySQL database
- **Data Profiling**: Generate data quality reports
- **Error Handling**: Comprehensive error handling and logging

## Data Sources

The pipeline processes the following e-commerce data:
- Categories, Customers, Inventory
- Orders and Order Items
- Payments and Products
- Returns, Reviews, and Shipping data

## Database Schema

The project includes a complete MySQL database schema with tables for all e-commerce entities and relationships between them.