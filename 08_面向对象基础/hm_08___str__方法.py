class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 我来了" % self.name)

    def __del__(self):  # 当cat对象不再使用了将会执行这个方法，相当于销毁
        print("%s 我走了" % self.name)

    def __str__(self):  # 在print输出对象时执行的方法，默认是输出内存地址，这里就是自定义了输出的内容
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name


tom = Cat("Tomcat")
print(tom.name)
print(tom)
