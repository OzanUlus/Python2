
# def counter(max):
#     number = 1
#     numbers = []

#     while number <= max:
#         numbers.append(number)
#         number += 1
#     return numbers

# result = counter(20)
# print(result) burada hafızada tutuyoruz ama biz hafızada tutmak istemiyoruz.


def counter(max):
    number = 1
  
    while number <= max:
        yield number
        number += 1
   
generator = counter(20)
# print(generator)
# print(dir(generator))
print(next(generator))
print(next(generator))
print(next(generator))

for i in generator:
    print(i)
