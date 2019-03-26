class Wages_Iterator:
    def __init__(self, wages):
        self.wages = wages
        self.pos = 0

    def __next__(self):
        if self.pos == len(self.wages):
            raise StopIteration
        else:
            self.pos += 1
            return self.wages[self.pos - 1]


class Wages:
    wages = [100, 120, 100, 140, 150, 180]

    def __iter__(self):
        return Wages_Iterator(self.wages)


w = Wages()
wi = iter(w)
print(wi.__next__())
print(wi.__next__())
wi2 = iter(w)
print(wi2.__next__())


# for n in w:
#     print(n)
