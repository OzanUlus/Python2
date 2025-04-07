import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "692619oU8587",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * from products WHERE id = 1"
# sql = "SELECT * from products WHERE id > 1"
# sql = "SELECT * from products WHERE name = 'Iphone 17'"
# sql = "SELECT * from products WHERE name = 'Iphone 17' and price = 80000"
# sql = "SELECT * from products WHERE name = 'Iphone 17' or price = 80000"
# sql = "SELECT * from products WHERE name LIKE '%Iphone%'"
# sql = "SELECT * from products WHERE name LIKE 'Iphone%'"
# sql = "SELECT * from products WHERE name LIKE '%Iphone'"
sql = "SELECT * from products WHERE name LIKE '%Iphone%' or description LIKE '%iyi%'"


# cursor.execute(sql)
cursor.execute(sql)

# result = cursor.fetchone()
result = cursor.fetchall()

def getProductById(id):
    sql = "SELECT * from products WHERE id = %s"
    params = (id,)
    cursor.execute(sql,params)
    result = cursor.fetchall()
    print(result)


getProductById(7)