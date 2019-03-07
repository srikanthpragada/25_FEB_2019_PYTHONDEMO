def add(n1, n2):  # keyword only arguments
    return n1 + n2


def total(*nums, n):
    return sum(nums)


def calculate(**values):
    pass


def two():
    return (10, 20)


calculate(x=10, y=20, z=30)

add(n2=1, n1=11)  # named params
add(n1=10, n2=20)  # positional params
total(10, 20, 30, n=30)
total(10, 20)
