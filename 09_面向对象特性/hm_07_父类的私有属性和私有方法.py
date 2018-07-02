class A:
    def __init__(self):
        self.num1 = 1
        self.__num2 = 2

    def __test(self):
        print("私有方法　%d %d" % (self.num1, self.__num2))


class B(A):  # 子类无法直接访问父类的私有属性和私有方法
    def test(self):
        # 除非在方法/属性前加上_类名，不然是无法使用私有对象的
        # super()._A__test()
        # print(self.num1, self._A__num2)
        pass

test = B()
test.test()
