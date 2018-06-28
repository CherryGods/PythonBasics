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
