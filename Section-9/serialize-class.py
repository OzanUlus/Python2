class Product:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

import json

#serialize
# p1 = Product(1, "Sansung S26", 70000)
# p2 = Product(2, "Sansung S27", 80000)

# # products = [p1.__dict__, p2.__dict__]

# products = {
#     p1.id : p1.__dict__,
#     p2.id : p2.__dict__

# }




# # with open("products3.json", "w") as file:
# #     json.dump(p1.__dict__, file)

# with open("products3.json", "w") as file:
#     json.dump(products, file)

#deserialize

with open("products3.json") as file:
    products = json.load(file)

print(type(products))

products2 = []
for key, value in products.items():
    products2.append(Product(key, value["title"], value["price"]))

print(type(products2))

for p in products2:
    print(p.title)
