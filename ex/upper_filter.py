def contains_upper(st):
    for c in st:
        if c.isupper():
            return True

    return False


names = ["Python", "c", "c++", "Java", "rubY"]
for n in filter(contains_upper, names):
    print(n)
