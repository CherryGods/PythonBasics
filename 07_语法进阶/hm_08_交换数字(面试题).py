a = 1
b = 200
# 解法１．使用其他变量
# c = a
# a = b
# b = c
# print(a, b)

# 解法２．不使用其他变量
# a = a + b
# b = a - b
# a = a - b
# print(a, b)

# 解法３．Python专有
# a, b = (b, a)
# 等号右边是一个元组，只不过把小括号省略了
a, b = b, a
print(a, b)
