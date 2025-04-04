
# lambda argument : expression

def takerSqrt(a):
    return a ** 2

result = takerSqrt(5)

result = (lambda a : a **2)(3)

takeSqrt = lambda a : a **2
result = takeSqrt(4)

total = lambda a,b,c : a + b + c

result = total(4,5,6)

def myFunc(n):
    return lambda a : a * n

x = myFunc(2)
y = myFunc(3)
z = myFunc(5)



result = x(3)
result = y(5)
result = z(8)




print(result)