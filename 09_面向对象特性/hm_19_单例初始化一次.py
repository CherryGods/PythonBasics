class MusicPlayer:
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否已经初始化
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 判断内存空间是否为空
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象
        return cls.instance

    def __init__(self):
        # 判断是否为已初始化
        if MusicPlayer.init_flag:
            return
        # 初始化
        print("初始化播放器")
        # 修改初始化标记
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
