def zero(n):
    print("Before change ", id(n))
    n = 0
    print("After change ", id(n))


v = 100
print(id(v))
zero(v)
print(v)
