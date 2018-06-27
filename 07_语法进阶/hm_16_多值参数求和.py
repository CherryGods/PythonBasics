def sum_result(*args):
    num = 0
    for n in args:
        num += n
    return num


result = sum_result(1, 2, 3, 4, 5)
print(result)
