class Cat:

    def eat(self):
        # 哪一个对象调用方法，那么self就是哪一个对象的引用
        print("%s 爱吃饭" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


cat = Cat()
# 这里是给这个对象的name赋值
cat.name = "Tom"
cat.eat()
cat.drink()
# 如果上面没有给cat对象的name赋值，而是在这里赋值的话将会报错，因为在调用方法前应该提前给这个属性赋值
cat.name = "Tom"
