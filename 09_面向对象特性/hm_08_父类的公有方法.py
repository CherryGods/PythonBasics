class A:
    def __init__(self):
        self.public_num = 1  # 公有属性
        self.__private_num = 2  # 私有属性

    def a_demo(self):  # 公有方法
        print("在公有方法中输出私有属性：%d" % self.__private_num)


class B(A):  # 子类可以直接在内部访问父类的公有属性和公有方法
    def b_demo(self):
        super().a_demo()  # 调用公有方法
        print(self.public_num)  # 调用公有属性


test = B()
test.b_demo()
