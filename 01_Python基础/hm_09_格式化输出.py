"""
格式化字符   含义
%s         字符串
%d         有符号的十进制整数，%06d 表示输出的整数显示位数，不足的地方使用0补全
%f         浮点数，%.02f代表显示两位小数

"""
# 定义一个字符串类型变量 name
name = "CherryGods"
# 输出　我的名字 CherryGods，请多多关照
print("我的名字 %s，请多多关照" % name)

# 定义一个整数变量　student_no
student_no = 10000
print("我的学号是%010d" % student_no)

# 定义小数　price,weight,money
price = 1.5
weight = 10
money = price * weight
print("单价:%.2f元／斤\t重量:%.2f斤\t\t金额:%.4f元" % (price, weight, money))

