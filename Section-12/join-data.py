import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "692619oU8587",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT name,categoryId FROM products"
# sql = "SELECT p.name,c.name FROM products p inner join categories c on p.categoryId=c.id"
# sql = "SELECT p.name,c.name FROM products p inner join categories c on p.categoryId=c.id WHERE c.id = 1"
sql = "SELECT p.name,c.name FROM products p inner join categories c on p.categoryId=c.id WHERE c.name='Telefon'"




cursor.execute(sql)

result = cursor.fetchall()

print(result)