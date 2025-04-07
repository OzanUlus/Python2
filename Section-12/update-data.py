import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "692619oU8587",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "UPDATE products SET name='Samsung S25-updated', price=price*1.2 WHERE id=1"
# cursor.execute(sql)

# try:
#     db.commit()
#     print(f"{cursor.rowcount} tane satır etkilendi.")
# except mysql.connector.Error as err:
#     print(err)
# finally:
#     db.close()
#     cursor.close()
#     print("bağlantı kapandı.")

def updateProduct(id,name,price):

    sql = "UPDATE products SET name=%s,price=%s WHERE id=%s"
    params = (name, price, id)
    cursor.execute(sql, params)

    try:
        db.commit()
        print(f"{cursor.rowcount} tane satır etkilendi.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()
        print("bağlantı kapandı.")

updateProduct(2,"Samsung S26-updated", 65000)
