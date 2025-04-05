
def selamlama(fn):
    def inner():
        print("Hoş Geldiniz.")
        fn()
        print("Görüşmek üzere.")
    return inner

@selamlama
def gunaydin():
    print("Günaydın benim adım Ozan")

@selamlama
def iyigunler():
    print("İyi günler benim adım Ozan")


# g = selamlama(gunaydin)
# i = selamlama(iyigunler)

# g()
# i()

gunaydin()
iyigunler()