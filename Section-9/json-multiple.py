db = {
    "users": {
        "ozanulus": {
            "firstname": "Ozan",
            "lastName": "Ulus"
        },
        "yaşaryıldırım": {
            "firstname": "Yaşar",
            "lastName": "Yıldırım"
        }
    },
    "products": {
        "1": {
            "title": "Macbook Pro",
            "price": 90000
        },
        "2": {
            "title": "HP Victus",
            "price": 40000
        },
        "3": {
            "title": "Asus",
            "price": 23000
        }
    }
}
import json
# with open("db.json", "w", encoding="utf-8") as file:
#     json.dump(db, file, ensure_ascii=False, indent=2)

with open("db.json", "r", encoding="utf-8") as file:
    datas = json.load(file)

print(datas["users"]["ozanulus"])
print(datas["products"])

datas["products"].update({
    "3": {
        "title": "Asus Zenbook",
        "price": 23000
    }
})
with open("db.json", "w", encoding="utf-8") as file:
    json.dump(datas, file, ensure_ascii=False, indent=2)


