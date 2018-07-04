def test():
    return 1 / int(input("请输入一个整数:"))


def test2():
    return test()


# 首先报错的是第二行代码,然后再将错误传递给test2()函数，然后再传递给print(test2())那一行代码
try:
    print(test2())
except ValueError:
    print("输入错误！只能输入整数！")
# 这样在捕获异常的时候只需要在最后一个传递点內进行代码异常捕获就好
