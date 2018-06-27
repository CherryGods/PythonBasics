# 定义一个函数sum_numbers
# 能够接收一个 num 的整数参数
# 计算　1+2+...num的结果
def sum_numbers(num):
    # 出口
    if num == 1:
        return 1
    temp = sum_numbers(num - 1)

    return num + temp


print(sum_numbers(3))
