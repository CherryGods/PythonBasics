class Tool():
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("剑")
# 对象名.类属性 = 值　这样并不会修改类属性的值
tool2.count = 0
print(tool2.count)  # 通过变量访问类型属性--不推荐
print(Tool.count)  # 通过类访问类属性
