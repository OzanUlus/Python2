import json

data = {
    "1": {
        "title": "Macbook Pro",
        "price": 90000
    },
    "2": {
        "title": "HP Victus",
        "price": 40000
    },
    "3": {
        "title": "Asus ZenBook",
        "price": 23000
    },
    "4": {
        "title": "Macbook Air",
        "price": 70000
    },
    "5": {
        "title": "Lenova Thinkpad",
        "price": 28000
    }
}

# with open("products2.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False, indent=2)



with open("products2.json", "r", encoding="utf-8") as file:
    products = json.load(file)


print(products["1"])
print(products["2"])

#add
# products.update({
#     "6": {
#         "title": "MSI",
#         "price": 26000
#     }
# })

#update
products.update({
    "3": {
        "title": "Asus",
        "price": 23000
    }
})

products.pop("6")

with open("products2.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)
