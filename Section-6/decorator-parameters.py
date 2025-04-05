
def double(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return inner

@double
def merhaba():
    print("merhaba")


@double
def selam(name):
    print(f"selam {name}")

@double
def iyigunler():
    return("İyi günler")

merhaba()
selam("Ozan")
print(iyigunler())