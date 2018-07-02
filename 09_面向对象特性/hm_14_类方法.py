class Tool:
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量：%d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("镐子")
# 调用类方法，直接类名.类方法名
Tool.show_tool_count()
