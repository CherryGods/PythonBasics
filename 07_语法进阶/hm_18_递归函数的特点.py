def sum_numbers(num):  # 递归要有参数
    print(num)
    # 递归要有出口，这里就是递归的出口，当条件满足时就退出
    if num == 1:
        return
    # 调用自身
    sum_numbers(num - 1)


sum_numbers(15)
