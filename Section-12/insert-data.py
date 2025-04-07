import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "692619oU8587",
    database = "shopdb"
)

cursor = db.cursor()

sql = "INSERT INTO products (Name,Price,ImageUrl,Description) VALUES (%s,%s,%s,%s)"
# value = ("Iphone 16",7000,"3.jpg","iyi bir telefon")
# cursor.execute(sql,value)
values = [
    ("HUAWEI Mate X6",109000,"7.jpg","iyi bir telefon"),
    ("HUAWEI Mate 50 Pro",36000,"8.jpg","iyi bir telefon"),
    ("HUAWEI Pura 70 Pro",50000,"9.jpg","iyi bir telefon")

    ]


cursor.executemany(sql,values)

try:
    db.commit()
    print(cursor.rowcount, "kayıt edildi.")
    print(f"son eklenen kaydın id: {cursor.lastrowid}")
except mysql.connector.Error as err:
    print("hata: ", err)
finally:
    cursor.close()
    db.close()
    print("bağlantı kapatıldı.")
