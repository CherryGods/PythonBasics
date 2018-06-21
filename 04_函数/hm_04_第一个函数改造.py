name = "小明"


# Python解释器知道下方定义了一个函数
def say():
    """打招呼"""
    print("你好")


print("我好")
# 只有在程序中，主动调用函数，才会让函数执行
# Pycharm中查看函数的文档注释快捷键Ctrl+Q
say()
print("%s好" % name)
