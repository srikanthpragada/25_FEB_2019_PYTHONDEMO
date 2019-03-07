def is_even(n):
    # print("Input ", n)
    return n % 2 == 0


def big_name(s):
    return len(s) > 4


l = [10, 11, 13, 16, 20]
# en = filter(is_even, l)
en = filter(lambda n: n % 2 == 0, l)

# Iterate over en
for n in en:
    print(n)

names = ["java", 'c', 'TypeScript', 'pythoN']
bignames = filter(big_name, names)
for n in bignames:
    print(n)
