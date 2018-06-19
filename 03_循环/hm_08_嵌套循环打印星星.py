row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*" * col)
        col += row
    row += 1
