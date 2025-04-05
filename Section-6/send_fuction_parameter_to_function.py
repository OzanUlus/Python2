
def filter(fn, list):
    result = []

    for item in list:
        if fn(item):
            result.append(item)

    return result

def isEven(num):
    return num % 2 == 0

def isPositive(num):
    return num > 0

numbers = [1,2,3,4,5,6,-1,-2,-3,-4]

result = filter(isEven,numbers)
result2 = filter(isPositive,numbers)

print(result)
print(result2)

