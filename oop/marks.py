class Marks_Iterator:
    def __init__(self, marks):
        self.pos = 0
        self.marks = marks

    def __next__(self):
        if self.pos == len(self.marks):
            raise StopIteration
        else:
            self.pos += 1
        return self.marks[self.pos - 1]


class Marks:
    def __init__(self):
        self.marks = [20, 30, 40, 25, 66]

    def add(self, m):
        self.marks.append(m)

    def __iter__(self):
        return Marks_Iterator(self.marks)


m = Marks()
mi1 = m.__iter__()
mi2 = m.__iter__()

print(mi1.__next__())
print(mi2.__next__())
