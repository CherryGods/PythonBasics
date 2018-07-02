class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("汪汪汪")


class XiaoTianQuan(Dog):
    def fly(self):
        print("哮天犬飞")

    def bark(self):  # 重写扩展父类的方法
        # super().bark()
        # python2.x中没有super()特殊类，我们可以使用父类.方法名(self)调用父类的方法
        # Dog.bark(self)
        # 注意:如果使用子类调用本方法，会出现递归调用的问题－死循环!
        # XiaoTianQuan.bark(self)
        print("$#&^*@#^$*&#@$")


xtq = XiaoTianQuan()
# 如果子类中重写了父类的方法，那么调用子类对象调用此方法会调用子类的方法，不会调用父类的方法
xtq.bark()
