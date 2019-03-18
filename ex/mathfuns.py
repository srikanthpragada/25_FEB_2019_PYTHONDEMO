# Module of math functions

if __name__ == '__main__':
    print("Mathfuns module is run")

def abs(n):
    if n >= 0:
        return n
    else:
        return n * -1


def is_even(n):
    return n % 2 == 0
