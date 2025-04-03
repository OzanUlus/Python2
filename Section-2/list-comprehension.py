numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)

numbers2 = [i * 2 for i in range(5)]

print(numbers2)

name = "Ozan Ulus"

for i in name:
    print(i.upper())

result = [i.upper() for i in name]
print(result)

