class Common:
    def process(self):
        print("Process in Common")


class A(Common):
    pass
    # def process(self):
    #     print("Process in A")


class B(Common):
    def process(self):
        print("Process in B")


class C(A, B):
    pass


obj_c = C()
obj_c.process()
print(C.__mro__)

