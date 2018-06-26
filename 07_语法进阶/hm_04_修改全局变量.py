# 全局变量
name = "菠萝"


def test01():
    global name
    name = "飞机"
    print(name)


def test02():
    name = "香蕉皮"
    print(name)


test01()
test02()
