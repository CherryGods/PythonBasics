row = 1
while row <= 5:
    col = 1
    while col <= row:
        # 打印小星星
        print("*", end="")
        col += 1
    # 在一行星星输出后添加的换行操作
    print("")
    row += 1
