class Dog:
    count = 0
    # 定义静态方法的前提，不使用类属性或者调用类方法/不使用实例属性或实例方法
    @staticmethod
    def run():
        print("小狗在跑步")


# 通过类名.静态方法名可以直接使用静态方法
Dog.run()
