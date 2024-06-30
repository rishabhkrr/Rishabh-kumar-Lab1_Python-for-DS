import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='loan',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE e_commerce")

    print("Database 'e_commerce' created successfully.")

except Error as e:
    print("Error while creating MySQL database: ", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# Define SQL queries
create_table_queries = [
    """CREATE TABLE supplier (
       SUPP_ID INT PRIMARY KEY,
       SUPP_NAME VARCHAR(50),
       SUPP_CITY VARCHAR(50),
       SUPP_PHONE VARCHAR(100)
    )""",
    """CREATE TABLE customer (
       CUS_ID INT PRIMARY KEY,
       CUS_NAME VARCHAR(20) DEFAULT NULL,
       CUS_PHONE VARCHAR(10),
       CUS_CITY VARCHAR(30),
       CUS_GENDER CHAR
    )""",
    """CREATE TABLE category (
       CAT_ID INT PRIMARY KEY,
       CAT_NAME VARCHAR(20)
    )""",
    """CREATE TABLE product (
       PRO_ID INT PRIMARY KEY,
       PRO_NAME VARCHAR(20),
       PRO_DESC VARCHAR(60),
       CAT_ID INT,
       FOREIGN KEY (CAT_ID) REFERENCES category(CAT_ID)
    )""",
    """CREATE TABLE product_details (
       PROD_ID INT PRIMARY KEY,
       PRO_ID INT,
       SUPP_ID INT,
       PROD_PRICE INT,
       FOREIGN KEY (PRO_ID) REFERENCES product(PRO_ID),
       FOREIGN KEY (SUPP_ID) REFERENCES supplier(SUPP_ID)
    )""",
    """CREATE TABLE orders (
       ORD_ID INT PRIMARY KEY,
       ORD_AMOUNT INT,
       ORD_DATE DATE,
       CUS_ID INT,
       PROD_ID INT,
       FOREIGN KEY (CUS_ID) REFERENCES customer(CUS_ID),
       FOREIGN KEY (PROD_ID) REFERENCES product_details(PROD_ID)
    )""",
    """CREATE TABLE rating (
       RAT_ID INT PRIMARY KEY,
       CUS_ID INT,
       SUPP_ID INT,
       RAT_RATSTARS INT,
       FOREIGN KEY (CUS_ID) REFERENCES customer(CUS_ID),
       FOREIGN KEY (SUPP_ID) REFERENCES supplier(SUPP_ID)
    )"""
]

insert_data_queries = {
    'supplier': [
        (1, 'Rajesh Retails', 'Delhi', '1234567890'),
        (2, 'Appario Ltd.', 'Mumbai', '258963147032'),
        (3, 'Knome products', 'Bangalore', '9785462315'),
        (4, 'Bansal Retails', 'Kochi', '8975463285'),
        (5, 'Mittal Ltd.', 'Lucknow', '7898456532')
    ],
    'customer': [
        (1, 'AAKASH', '9999999999', 'DELHI', 'M'),
        (2, 'AMAN', '9785463215', 'NOIDA', 'M'),
        (3, 'NEHA', '9999999998', 'MUMBAI', 'F'),
        (4, 'MEGHA', '9994562399', 'KOLKATA', 'F'),
        (5, 'PULKIT', '7895999999', 'LUCKNOW', 'M')
    ],
    'category': [
        (1, 'BOOKS'),
        (2, 'GAMES'),
        (3, 'GROCERIES'),
        (4, 'ELECTRONICS'),
        (5, 'CLOTHES')
    ],
    'product': [
        (1, 'GTA V', 'DFJDJFDJFDJFDJFJF', 2),
        (2, 'TSHIRT', 'DFDFJDFJDKFD', 5),
        (3, 'ROG LAPTOP', 'DFNTTNTNTERND', 4),
        (4, 'OATS', 'REURENTBTOTH', 3),
        (5, 'HARRY POTTER', 'NBEMCTHTJTH', 1)
    ],
    'product_details': [
        (1, 1, 2, 1500),
        (2, 3, 5, 30000),
        (3, 5, 1, 3000),
        (4, 2, 3, 2500),
        (5, 4, 1, 1000)
    ],
    'orders': [
        (20, 1500, '2021-10-12', 3, 5),
        (25, 30500, '2021-09-16', 5, 2),
        (26, 2000, '2021-10-05', 1, 1),
        (30, 3500, '2021-08-16', 4, 3),
        (50, 2000, '2021-10-06', 2, 1)
    ],
    'rating': [
        (1, 2, 2, 4),
        (2, 3, 4, 3),
        (3, 5, 1, 5),
        (4, 1, 3, 2),
        (5, 4, 5, 4)
    ]
}




# Execute queries
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='e_commerce',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        cursor = connection.cursor()

        # Create tables
        for query in create_table_queries:
            cursor.execute(query)
        print("Tables created successfully.")

        # Insert data into tables
        for table, data in insert_data_queries.items():
            for row in data:
                placeholders = ', '.join(['%s'] * len(row))
                query = f"INSERT INTO {table} VALUES ({placeholders})"
                cursor.execute(query, row)
        print("Data inserted successfully.")

        # Committing the changes and closing connection
        connection.commit()

except Error as e:
    print("Error executing queries:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")




