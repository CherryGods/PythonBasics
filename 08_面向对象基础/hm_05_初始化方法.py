class Cat:
    def __init__(self):  # 初始化方法，是系统函数，这里是当创建Cat对象时就会被立刻执行的方法
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃饭" % self.name)


tom = Cat()
print(tom.name)
