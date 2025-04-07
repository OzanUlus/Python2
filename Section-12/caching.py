import mysql.connector
from cachetools import cached,TTLCache

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "692619oU8587",
    database = "shopdb"
)


@cached(cache=TTLCache(maxsize=32, ttl=60))
def getProducts():
    cursor = db.cursor()
    sql = "SELECT p.name,c.name FROM products p inner join categories c on p.categoryId=c.id WHERE c.name='Telefon'"
    cursor.execute(sql)
    print("from sql")
    return cursor.fetchall()

print(getProducts())
print(getProducts())
print(getProducts())

    