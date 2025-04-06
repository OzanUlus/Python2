import json
data = [
    {
    "id": 1,
    "title": "Macbook Pro",
    "price": 90000
    },
    {
        "id": 2,
        "title": "HP Victus",
        "price": 40000
    },
    {
        "id": 3,
        "title": "Asus Zonebook",
        "price": 23000
    },
    {
        "id": 4,
        "title": "Macbook Air",
        "price": 70000
    }
]
# with open("products.json", "w", encoding="utf-8") as file:
#     json.dump(data,file, ensure_ascii=False, indent=2)

product = {
    
        "id": 5,
        "title": "Lenova Thinkpad",
        "price": 28000
    
    }

with open("products.json") as  file:
    products = json.load(file)

# products.append(product) ürün ekleme

#update
for p in products:
    if p["title"] == "Asus Zonebook":
        p["title"] = "Asus ZenBook"

products.remove(products[3])


with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products,file, ensure_ascii=False, indent=2)
