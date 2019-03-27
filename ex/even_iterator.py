class EvenNumbers_Iterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 2
            return self.start - 2


class EvenNumbers:
    def __init__(self, start, end):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        return EvenNumbers_Iterator(self.start, self.end)


en = EvenNumbers(1, 10)

for n in en:
    print(n)

for n in en:
    print(n)
