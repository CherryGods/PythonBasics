class Cat:  # 定义猫类

    def eat(self):
        print("小猫爱吃饭")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
cat = Cat()
cat.eat()
cat.drink()
print(cat)
addr = id(cat)
print(addr)
