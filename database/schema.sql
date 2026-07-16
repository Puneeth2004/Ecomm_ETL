-- creating a database 

CREATE DATABASE IF NOT EXISTS ecomm_db;
USE ecomm_db;



CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    gender VARCHAR(10) NOT NULL,
    city VARCHAR(50),
    state VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    signup_date DATE NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    brand VARCHAR(100) NOT NULL,
    cost_price DECIMAL(10,2) NOT NULL,
    selling_price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL,

    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);


CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY,
    product_id INT NOT NULL,
    warehouse VARCHAR(100) NOT NULL,
    stock_quantity INT NOT NULL,
    reorder_level INT,
    last_restock_date DATE NOT NULL,

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(30) NOT NULL,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);



CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount DECIMAL(10,2),
    line_total DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);


CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method VARCHAR(50),
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    payment_date DATE NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);


CREATE TABLE shipping (
    shipping_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    carrier VARCHAR(100),
    shipping_date DATE NOT NULL,
    delivery_date DATE NOT NULL,
    shipping_cost DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);


CREATE TABLE returns (
    return_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    return_reason VARCHAR(255),
    return_date DATE NOT NULL,
    refund_amount DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);


CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    order_id INT NOT NULL,
    rating INT NOT NULL,
    review_text TEXT,
    review_date DATE NOT NULL,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

show tables;
describe customers;
describe orders;