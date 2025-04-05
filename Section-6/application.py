import time

def speed_test(fn):
    def inner(*args, **kwargs):
        star_time = time.perf_counter()
        print(f"{fn.__name__} metodu çalışıyor.")
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - star_time
        print(f"Geçen süre {run_time}")
        return result
    return inner
    


@speed_test
def sum_gen():
    return sum((i for i in range(1000000)))


@speed_test
def sum_list():
    return sum([i for i in range(1000000)])


print(sum_list())
print(sum_gen())