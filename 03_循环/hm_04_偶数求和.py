# 能被整除的都是偶数
i = 0
sum_number = 0
while i <= 4:
    if i % 2 == 0:
        sum_number += i
    i += 1
print(sum_number)
