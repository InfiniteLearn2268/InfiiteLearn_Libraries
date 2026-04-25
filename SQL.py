import sqlite3

# -------------------- EMP TABLE (BASIC PRACTICE) --------------------

# conn = sqlite3.connect('databasd.db')
# cursor = conn.cursor()

# # CREATE TABLE
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS emp(
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL,
#     dept TEXT NOT NULL
# )
# ''')

# conn.commit()

# # DELETE ALL DATA
# cursor.execute("DELETE FROM emp")

# # INSERT DATA
# cursor.execute('''
# INSERT INTO emp(name, age, dept) VALUES('shri', 23, 'Ai')
# ''')

# cursor.execute('''
# INSERT INTO emp(name, age, dept) VALUES('bhavesh', 22, 'Ds')
# ''')

# cursor.execute('''
# INSERT INTO emp(name, age, dept) VALUES('abhi', 23, 'Cs')
# ''')

# conn.commit()

# # SELECT DATA
# cursor.execute("SELECT * FROM emp")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# # UPDATE
# cursor.execute('''
# UPDATE emp
# SET name = 'king'
# WHERE name = 'bhavesh'
# ''')

# conn.commit()

# cursor.execute("SELECT * FROM emp")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# # DELETE
# cursor.execute('''
# DELETE FROM emp
# WHERE name = 'bhavesh'
# ''')

# conn.commit()

# cursor.execute("SELECT * FROM emp")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)


# -------------------- REAL LIFE DATA SCIENCE APPLICATION --------------------

conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# CREATE TABLE
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sale INTEGER NOT NULL,
    region TEXT NOT NULL
)
''')

conn.commit()

# DATA
sales_data = [
    ('2023-01-01', 'product1', 100, 'North'),
    ('2023-01-02', 'product2', 100, 'South'),
    ('2023-01-03', 'product3', 100, 'West'),
    ('2023-01-04', 'product4', 100, 'East'),
    ('2023-01-05', 'product5', 100, 'West')
]

# INSERT (optional - currently commented)
# cursor.executemany('''
# INSERT INTO sales(date, product, sale, region)
# VALUES (?, ?, ?, ?)
# ''', sales_data)
#
# conn.commit()

# UPDATE (optional - commented)
# cursor.execute('''
# UPDATE sales
# SET product = 'grocery'
# WHERE date = '2023-01-01'
# ''')
#
# conn.commit()

# DELETE
cursor.execute('''
DELETE FROM sales
WHERE product = 'product1'
''')

conn.commit()

# SELECT
cursor.execute("SELECT * FROM sales")
rows = cursor.fetchall()

for row in rows:
    print(row)

# CLOSE
conn.close()   # AFTER THESE LINE YOU ARE NOT ABLE TO WRITE ANY QUERY LIKE cursor.execute( Delete , insert or any other )


# UPCOMIN IS : MULTITHREADING AND MULTIPROCESSING