class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 我来了" % self.name)

    def __del__(self):  # 当cat对象不再使用了将会执行这个方法，相当于销毁
        print("%s 我走了" % self.name)


tom = Cat("Tomcat")
print(tom.name)

# del关键字可以删除一个对象
del tom
print("-" * 50)
