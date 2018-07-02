class Father:
    def play(self):
        print("爱玩")

    def buy(self):
        print("爸爸爱买")


class Mother:
    def eat(self):
        print("爱吃")

    def buy(self):
        print("妈妈爱买")


class Son(Father, Mother):  # 在父类有相同的方法时，应当避免使用多继承
    def cry(self):
        print("爱哭")

    # 遗传下来的方法
    def inheritance(self):
        # 可以直接使用父类的方法
        super().play()
        super().eat()
        # 如果父类同时存在相同的方法，那么会执行继承的第一个父类的方法．
        super().buy()


xiao_ming = Son()
xiao_ming.inheritance()
xiao_ming.cry()
print(Son.mro())
# 从左往右查找，如果找到方法名为所执行的方法名相同则执行，否则继续查找，当依次查找且未查到的话程序会报错
# [<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]
