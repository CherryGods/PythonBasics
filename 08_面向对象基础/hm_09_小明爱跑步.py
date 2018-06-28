class Person:

    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s,体重是%.2fkg" % (self.name, self.weight)

    def eat(self):
        print("%s在吃饭,体重增加了%.2fkg" % (self.name, 1))
        self.weight += 1

    def run(self):
        print("%s在跑步,体重减少了%.2fkg" % (self.name, 0.5))
        self.weight -= 0.5


p1 = Person("小明", 70)
p1.eat()
p1.run()
print(p1)
