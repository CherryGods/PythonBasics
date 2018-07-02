class Father:
    def play(self):
        print("爱玩")


class Mother:
    def eat(self):
        print("爱吃")


class Son(Father, Mother):
    def cry(self):
        print("爱哭")

    # 遗传下来的方法
    def inheritance(self):
        # 可以直接使用父类的方法
        super().play()
        super().eat()


xiao_ming = Son()
xiao_ming.inheritance()
xiao_ming.cry()

