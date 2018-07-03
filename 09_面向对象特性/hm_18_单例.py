class MusicPlayer:
    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断内存空间是否为空
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象
        return cls.instance


# 创建多个对象
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
