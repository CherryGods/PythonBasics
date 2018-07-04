def input_password():
    pwd = input("请输入密码(长度必须大于5):")

    if len(pwd) > 5:
        return pwd

    # 创建异常对象
    ex = Exception("密码长度必须大于5")
    # 主动抛出异常对象
    raise ex


try:
    print(input_password())
except Exception as e:
    print(e)
