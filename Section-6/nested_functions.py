# def comminication(name):
#     return f"Hi, {name}"

# hello = comminication

# print(hello)
# print(comminication)

# # print(comminication("Ozan"))
# # print(hello("Ozan"))

# del comminication

# print(hello)
# # print(comminication("Ozan"))
# print(hello("Ozan"))

#nested

def outer(number):
    def inner(number):
        print(number)

    inner(number)

outer(12)


def factorial(number):

    if not isinstance(number, int):
        raise TypeError("number must be int")
    if not number >= 0:
        raise ValueError("number must be 0 or bigger")
    def innerFactorial(number):
        if number <= 1:
            return 1
        
        return number * innerFactorial(number - 1)
        
    return innerFactorial(number)

result = factorial(5)
# result = factorial("a")
# result = factorial(-4)
result = factorial(10)
print(result)




