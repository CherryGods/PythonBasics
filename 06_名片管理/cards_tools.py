# 名片列表
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用［名片管理系统］V1.0", end="\n\n")
    print("1.新建名片\n2.显示全部\n3.查询名片\n\n0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入详细信息
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入QQ:")
    email = input("请输入邮箱:")
    # 2.根据信息追加名片字典
    card_dict = {"name": name,
                 "phone": phone,
                 "qq:": qq,
                 "email": email}
    # 3.将名片字典添加到名片列表
    card_list.append(card_dict)
    # 4.提示用户添加成功
    print("添加%s成功!" % name)


def show_all():
    """显示全部"""
    print("-" * 50)
    print("显示全部")
    print(card_list)


def find_card():
    """查询名片"""
    print("-" * 50)
    print("查询名片")
