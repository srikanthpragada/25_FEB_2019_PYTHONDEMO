class A:
    def process(self):
        print('A process()')


class B(A):
    def process(self):
        print('B process()')


class C(B,A):
    pass


obj = C()
obj.process()
print(C.__mro__)