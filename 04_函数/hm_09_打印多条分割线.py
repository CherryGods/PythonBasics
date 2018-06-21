def print_line(char, times):
    """
    打印分割线
    :param char:　要打印的字符
    :param times: 要打印的次数
    :return:
    """
    print(char * times)


print_line("-", 20)


def print_lines(char, times):
    row = 0
    while row < times:
        print_line(char, times)
        row += 1


print_lines("=", 20)
