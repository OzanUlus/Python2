import time
import threading

def calculate_sqr(numbers):
    print("sayıların kareleri hesaplanıyor...")

    for i in numbers:
        time.sleep(0.3)
        print("kare: ", i * i)

def calculate_cube(numbers):
     print("sayıların küpleri hesaplanıyor...")

     for i in numbers:
        time.sleep(0.3)
        print("küp: ", i * i * i)

numbers = [3,5,8,9,15,25]

t = time.time()

# calculate_sqr(numbers)
# calculate_cube(numbers)

t1 = threading.Thread(target=calculate_sqr, args=(numbers,))
t2 = threading.Thread(target=calculate_cube, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()




print("işlem tamamlandı.", time.time() - t)

  