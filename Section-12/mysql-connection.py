import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "692619oU8587",
    database = "shopdb"
)

print(db)

cursor = db.cursor()
# cursor.execute("CREATE DATABASE exampledb")
# cursor.execute("SHOW DATABASES")
# cursor.execute("CREATE TABLE categories (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
cursor.execute("SHOW TABLES")
for i in cursor:
    print(i)


