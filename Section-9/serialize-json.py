import json

product = {
    "id": 2,
    "title": "Macbook Pro",
    "price": 90000,
    "rating": "4.5",
    "category": "Computer",
    "color": ["Red", "Blue"]
}

print(product)
print(type(product))

# result = json.dumps(product)
# print(result)
# print(type(result))

with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product,file, ensure_ascii=False, indent=2)
