import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "692619oU8587",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "DELETE FROM products WHERE id=1"
sql = "DELETE FROM products WHERE name LIKE '%Mate 50%'"

cursor.execute(sql)

try:
    db.commit()
    print(f"{cursor.rowcount} tane kayıt silindi.")
except mysql.connector.Error as err:
    print(err)
finally:
    db.close()
    cursor.close()