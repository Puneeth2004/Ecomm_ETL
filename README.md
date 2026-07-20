#  E-Commerce ETL Analytics Pipeline

> An end-to-end Data Engineering project that extracts, validates, transforms, and loads E-Commerce data into a normalized MySQL database, followed by SQL analytics and interactive Power BI dashboards.

---

#  Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline built using Python, Pandas, SQLAlchemy, and MySQL. The pipeline processes raw E-Commerce datasets, performs data quality validation, applies transformations, and loads the cleaned data into a relational database for business analytics.

The project also includes advanced SQL analytical queries and a Power BI dashboard for generating business insights.

---

#  Project Architecture

```
                Raw CSV Files
                      │
                      ▼
            Extract Data (Python)
                      │
                      ▼
         Data Validation (Quality Checks)
                      │
                      ▼
        Data Transformation & Cleaning
                      │
                      ▼
            Load into MySQL Database
                      │
                      ▼
             SQL Analytics Reports
                      │
                      ▼
          Interactive Power BI Dashboard
```

---

#  Features

- Automated extraction of multiple CSV datasets
- Data quality validation
- Missing value detection
- Duplicate record detection
- Invalid email validation
- Data transformation and cleaning
- Date conversion
- Schema validation
- Automated MySQL loading using SQLAlchemy
- Normalized relational database design
- Advanced SQL analytics
- Interactive Power BI dashboard
- Modular ETL architecture

---

#  Tech Stack

## Programming

- Python 3.x
- SQL

## Libraries

- Pandas
- SQLAlchemy
- PyMySQL

## Database

- MySQL

## Visualization

- Power BI

## Tools

- VS Code
- MySQL Workbench
- Git
- GitHub

---

#  Project Structure

```
Ecommerce-ETL-Analytics
│
├── data
│   ├── raw
│   ├── cleaned
│   └── processed
│
├── database
│   └── schema.sql
│
├── etl
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   ├── load.py
│   └── mapping.py
│
├── reports
│   └── data_quality_report.csv
│
├── sql
│   ├── 01_basic_queries.sql
│   ├── 02_join_queries.sql
│   ├── 03_aggregation_queries.sql
│   ├── 04_window_functions.sql
│   ├── 05_cte_queries.sql
│   └── 06_business_kpis.sql
│
├── dashboard
│   ├── Ecommerce_Dashboard.pbix
│   ├── dashboard_page1.png
│   └── dashboard_page2.png
│
├── screenshots
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

#  Database Schema

The project uses a normalized relational database consisting of the following tables:

- Categories
- Customers
- Products
- Inventory
- Orders
- Payments *(currently excluded from dashboard due to source data integrity issues)*
- Shipping
- Returns
- Reviews
- Order Items

The schema includes:

- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- Normalized Design

---

# ETL Workflow

## 1️ Extract

Reads multiple CSV datasets dynamically.

Datasets include:

- Categories
- Customers
- Products
- Inventory
- Orders
- Payments
- Shipping
- Returns
- Reviews
- Order Items

---

## 2️ Validate

Performs multiple data quality checks including:

- Missing Values
- Duplicate Rows
- Duplicate Emails
- Invalid Emails
- Negative Prices
- Selling Price below Cost
- Negative Quantity
- Invalid Ratings

Generates:

```
reports/data_quality_report.csv
```

---

## 3️ Transform

Applies the following transformations:

- Date Conversion
- Text Cleaning
- Lowercase Emails
- Missing Value Handling
- Duplicate Removal
- Schema Mapping

---

## 4️ Load

Loads transformed data into MySQL using SQLAlchemy.

Features:

- Connection Validation
- Schema Validation
- Batch Loading
- Table Truncation
- Error Handling

---

#  SQL Analytics

The project includes more than 50 SQL queries organized into the following modules:

### Basic Queries

- Record Counts
- Filtering
- Sorting

### Join Queries

- Customer Orders
- Product Details
- Order Summary
- Inventory Reports

### Aggregation Queries

- Revenue Analysis
- Category Sales
- Customer Distribution
- Product Ratings

### Window Functions

- RANK()
- DENSE_RANK()
- ROW_NUMBER()
- LAG()
- LEAD()

### Common Table Expressions (CTEs)

- Top Customers
- Revenue Reports
- Inventory Analysis

### Business KPIs

- Revenue
- Orders
- Customers
- Products
- Inventory
- Returns
- Ratings

---

#  Power BI Dashboard

The dashboard provides interactive business insights including:

## Executive Dashboard

- Total Revenue
- Total Orders
- Total Customers
- Total Products
- Average Rating
- Returns Analysis

## Visualizations

- Revenue Trend
- Revenue by Category
- Top Products
- Inventory by Warehouse
- Customer Distribution
- Product Ratings
- Return Analysis

<img width="1525" height="873" alt="image" src="https://github.com/user-attachments/assets/4e004a71-301d-4a6e-9b13-0a183cebbb0e" />


#  Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Ecommerce-ETL-Analytics.git
```

Move into the project directory

```bash
cd Ecommerce-ETL-Analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

#  Running the ETL Pipeline

Configure your MySQL credentials inside:

```
config.py
```

Run the ETL pipeline

```bash
py main.py
```

---

#  SQL Analytics

Open the SQL files inside the `sql/` directory using MySQL Workbench and execute them sequentially.

```
01_basic_queries.sql

↓

02_join_queries.sql

↓

03_aggregation_queries.sql

↓

04_window_functions.sql

↓

05_cte_queries.sql

↓

06_business_kpis.sql
```

---

#  Power BI

1. Open

```
dashboard/Ecommerce_Dashboard.pbix
```

2. Refresh the MySQL connection.

3. Explore the interactive dashboard.

---

#  Known Limitation

The `payments` table is currently excluded from dashboard analytics due to source data integrity issues encountered during ETL loading. This does not impact the remaining analytics pipeline or dashboard functionality.

---

#  Future Enhancements

- Apache Airflow Scheduling
- Docker Containerization
- Incremental ETL Loading
- AWS S3 Integration
- Azure Data Factory
- Snowflake Data Warehouse
- Apache Spark ETL
- Real-Time Kafka Streaming

---

#  Learning Outcomes

This project demonstrates practical experience with:

- ETL Pipeline Development
- Data Validation
- Data Cleaning
- Relational Database Design
- SQL Analytics
- Window Functions
- Common Table Expressions
- Data Visualization
- Power BI
- Python Automation
- Data Engineering Best Practices

---

#  Author

**Puneeth K**

Final Year Integrated M.Tech Computer Science Student

Aspiring Data Engineer

GitHub: https://github.com/Puneeth2004

LinkedIn: www.linkedin.com/in/puneeth-k-05254824b

---

#  If you found this project useful, consider giving it a Star!
