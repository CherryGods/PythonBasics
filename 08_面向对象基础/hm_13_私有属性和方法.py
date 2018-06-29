class Women:
    def __init__(self, name):
        self.name = name
        # 创建私有属性
        self.__age = 18

    def __secret(self):  # 创建私有方法｀
        print("%s 的年龄是 %d" % (self.name, self.__age))

    def a(self):
        self.__secret()


xiaomei = Women("小美")
# 私有属性,在外界无法直接访问
# print(xiaomei.__age)
# 私有方法,在外界同样无法直接访问
# xiaomei.__secret()
xiaomei.a()
