# for item in list:
#     if(condition):
#         expression

# [expression for item in list if condition]

numbers = [3,5,7,6,56,34]
result = []

for number in numbers:
    if(number % 2 == 0):
        result.append(number)
print(result)

result2 = [number for number in numbers if number % 2 ==0 ]
result2 = [number if number % 2 ==0 else "tek sayı" for number in numbers] # bana her değer gelsin ama gelen her sayı üzerinde farklı işlem yapacağım.

print(result2)

productPrices = [3000,1000,4000,0,5000]
priceWithTax = []

for price in productPrices:
    if(price > 0):
        priceWithTax.append(price * 1.20)

print(priceWithTax)

priceWithTax2 = [price * 1.20 for price in productPrices if price > 0]

priceWithTax3 = [price * 1.20 if price > 0 else "not calculate tax" for price in productPrices ]

print(priceWithTax2)
print(priceWithTax3)
