def wages():
    w = [100,120,100,140,150,160,200]
    for n in w:
        yield n


print(wages)
print(wages())

for n in wages():
    print(n)