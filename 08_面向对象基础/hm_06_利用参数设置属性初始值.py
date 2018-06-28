class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # 设置初始化name
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s 爱吃饭" % self.name)


tom = Cat("Tomcat")  # 传递参数给init()方法，方法內的作用是将接收到的参数传递给self.name
tom.eat()
print(tom.name)
