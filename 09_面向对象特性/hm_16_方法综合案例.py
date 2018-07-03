class Game(object):
    # 历史最高分
    top_score = 0

    # 初始化人物信息
    def __init__(self, name):
        self.player_name = name

    # 查看帮助信息
    @staticmethod
    def show_help():
        print("帮助信息: 让僵尸进入大门")

    # 查看历史最高分
    @classmethod
    def show_top_score(cls):
        print("历史最高分:%d" % cls.top_score)

    # 开始游戏
    def start_game(self):
        print("%s 开始了游戏..." % self.player_name)


# 1.查看帮助信息
Game.show_help()
# 2.查看历史最高分
Game.show_top_score()
# 3.开始游戏
player = Game("CherryGods")
player.start_game()

