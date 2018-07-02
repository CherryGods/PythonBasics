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


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


class XiaoTianQuan(Dog):
    def fly(self):
        print("哮天犬飞")


xtq = XiaoTianQuan()
xtq.bark()
xtq.fly()
# 哮天犬和猫有不同的继承关系，虽然他们的祖类都是动物类但是由于哮天犬和猫类没有直接的继承关系所以无法使用父类的方法和属性
# xtq.catch()
