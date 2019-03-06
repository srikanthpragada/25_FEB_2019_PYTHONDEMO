def add(n1, n2):  # keyword only arguments
    return n1 + n2


def total(*nums):
    pass


add(n2=1, n1=11)  # named params
add(n1=10, n2=20)  # positional params
total(10,20,30,30)

