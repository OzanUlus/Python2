
# def createNumber():
#     number = 0
#     while True:
#         yield number ** 2
#         number +=1

# generator = createNumber()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)


# def fibGen(max):
#     a, b = 0, 1
#     count = 0
#     while count <= max:
#         a, b = b, a + b
#         yield b
#         count += 1

# for i in fibGen(90000):
#     print(i)

import sys

liste = [i for i in range(10000)]
print(sys.getsizeof(liste))

gen = (i for i in range(10000))
print(sys.getsizeof(gen))

import time

list_start_time = time.time()
sum([i for i in range(9000000)])
list_stop = time.time() - list_start_time

gen_start_time = time.time()
sum((i for i in range(9000000)))
gen_stop = time.time() - gen_start_time

print(list_stop)
print(gen_stop)




