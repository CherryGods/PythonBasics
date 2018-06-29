class Gun:
    def __init__(self, module):
        # 1.枪的型号
        self.module = module
        # 2.枪的子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        # 装弹
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count > 0:
            # 2.发射子弹，子弹-1
            self.bullet_count -= 1
            # 3.提示发射信息
            print("[%s] 突突突...[%d]" % (self.module, self.bullet_count))
        else:
            print("[%s]　没有子弹了..." % self.module)


class Soldier:
    def __init__(self, name):
        # 1.姓名
        self.name = name
        # 2.枪，新兵没有枪
        # 如果不知道设置什么初始值，可以设置为None，代表什么都没有，空对象
        self.gun = None


# 1. 创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(35)
ak47.shoot()

xusanduo = Soldier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun)
