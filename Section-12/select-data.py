import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "692619oU8587",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products"
sql = "SELECT id,name FROM products"


cursor.execute(sql)

# products = cursor.fetchall()
# for p in products:
#     print(p)
product = cursor.fetchone()
print(product)



