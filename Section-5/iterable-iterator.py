#iterable
#iterator

numbers = [1,2,3,4,5]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break

# print(next(iterator)) tek tek yazıyor.

