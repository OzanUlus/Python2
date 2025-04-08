import time
import multiprocessing




def calculate_sqr(numbers, list_):
    global list_sqr
    print("sayıların kareleri hesaplanıyor...")

    for index, value in enumerate(numbers):
        time.sleep(0.3)
        list_[index] = value * value

def calculate_cube(numbers, list_):
     global list_cube
     print("sayıların küpleri hesaplanıyor...")

     for index, value in enumerate(numbers):
        time.sleep(0.3)
        list_[index] = value * value * value

if __name__ == "__main__":
    arr = [2,4,5,6,8,12,56]

    t = time.time()

    list_sqr =  multiprocessing.Array('i', len(arr))
    list_cube = multiprocessing.Array('i', len(arr))

    p1 = multiprocessing.Process(target=calculate_sqr, args=(arr, list_sqr))
    p2 = multiprocessing.Process(target=calculate_cube, args=(arr, list_cube))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(time.time() - t)

    t = time.time()

    # calculate_sqr(arr)
    # calculate_cube(arr)

    print(list_sqr[:])
    print(list_cube[:])




    # print(time.time() - t)
