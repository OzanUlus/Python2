numbers = [1,2,3,4,5]
numbers_str = ["1","2","3","4","5"]
names = ["ozan", "yaşar","berkalp"]
users = [
    {"name" : "ozan", "surname" : "ulus"},
    {"name" : "yaşar", "surname" : "yıldırım"},
    {"name" : "berkalp", "surname" : "direm"},

    ]

# sqrt = []

# for number in numbers:
#     sqrt.append(number ** 2)

# print(sqrt)

def takeSqrt(number):
    return number ** 2


result =list( map(takeSqrt,numbers))

print(result)

result2 =list( map(lambda number : number ** 2,numbers))
result2 =list( map(int, numbers))
result2 =list( map(str.capitalize, names))
result2 =list( map(lambda person : person["name"].upper(),users))




print(result2)