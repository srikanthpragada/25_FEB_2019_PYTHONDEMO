def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def abs(n1):
    return n1


def calculate(n1, n2, task):
    return task(n1, n2)


print(calculate(10, 20, add))
print(calculate(10, 20, mul))
# print(calculate(10, 20, abs))
