class Music_Play():
    def __new__(cls, *args, **kwargs):
        print("创建对象,分配空间")
        # 重写__new__方法必须返回分配的内存空间
        return super().__new__(cls)

    def __init__(self):
        print("初始化播放器")


music_play = Music_Play()
print(music_play)