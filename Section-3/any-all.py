# any all

result = all([True,True,False]) #result false
result = all([True,True,True]) #result true
result = any([True,True,True]) #result true
result = any([True,True,False]) #result true

# and => True and True => all()
# or => True and False => any()

numbers = [1,3,5,7,6,8,0]

result = all([bool(number) for number in numbers])
result = any([bool(number) for number in numbers])
result = all([number % 2 == 0 for number in numbers])
result = any([number % 2 == 0 for number in numbers])





print(result)

