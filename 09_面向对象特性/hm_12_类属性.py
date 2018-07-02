class Tool():
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("剑")
print(Tool.count)  # 通过类访问类属性
print(tool2.count)  # 通过变量访问类型属性--不推荐
