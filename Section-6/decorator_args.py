# def dec_selamlama(count):
#     def selamlama(fn):
#         def inner(ad):
#             for _ in range(count):
#                 fn(ad)
#         return inner
#     return selamlama

# @ dec_selamlama(count=2)
# def gunaydin(ad):
#     print(f"Günaydın benim adım {ad}")

# @ dec_selamlama(count=2)
# def iyigunler(ad):
#     print(f"İyi günler benim adım {ad}")


# gunaydin("ozan")
# iyigunler("yaşar")

import time
def dec_speed(count):
    def speed_test(fn):
        def inner(*args, **kwargs):
            star_time = time.perf_counter()
            print(f"{fn.__name__} metodu çalışıyor.")
            for _ in range(count):
                result = fn(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - star_time
                print(f"Geçen süre {run_time}")
            return result
        return inner
    return speed_test
        


@dec_speed(count=2)
def sum_gen():
    return sum((i for i in range(10000000)))


@dec_speed(count=3)
def sum_list():
    return sum([i for i in range(10000000)])


print(sum_list())
print(sum_gen())