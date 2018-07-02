class Dog(object):  # 旧类，为了兼容python2,x
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s 在天上快乐的玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        dog.game()


# 1.创建狗对象
# wangcai = Dog("旺财")
xtq = XiaoTianQuan("哮天犬")
# 2.创建人对象
xiaoming = Person("小明")
# 3.让人和狗玩
xiaoming.game_with_dog(xtq)
