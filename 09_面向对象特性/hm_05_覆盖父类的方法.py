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

    def bark(self):  # 重写父类的方法
        print("无敌大叫，神狗叫")


xtq = XiaoTianQuan()
# 如果子类中重写了父类的方法，那么调用子类对象调用此方法会调用子类的方法，不会调用父类的方法
xtq.bark()
