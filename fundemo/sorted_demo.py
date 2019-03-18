names = ["Stephen", "Joe", "Mi", "Andy"]

for n in sorted(names):
    print(n)

for n in sorted(names, key=len):
    print(n)
