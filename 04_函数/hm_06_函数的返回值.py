def sum_num(num1, num2):  # 里面的参数叫做形参
    """
    双数求和
    :param num1: 数字１
    :param num2: 数字２
    :return: 结果
    """
    return num1 + num2


# 定义一个变量来接收返回值
result = sum_num(10, 20) # 里面的参数叫做实参
print("结果:%d" % result)
