import json
# with open("product.json") as file:
#     data = json.load(file)             #başka sayfadan okuma yap.

data = """
{
    "id": 1,
    "title": "Macbook Pro",
    "price": 90000,
    "rating": "4.5",
    "category": "Computer",
    "color": ["Red", "Blue"]
}
"""
data = json.loads(data) #başka sayfadan değil olduğumuz sayfadan okuma yapacaksak loads kullan.

print(data)
print(type(data))
print(data["title"])
print(data["price"])
print(data["color"])


#Deserialize => decode
#Serialize => encode


