# 格式化字符串后面的'()'本质上就是元组
info_tuple = ('CherryGods', 16)
print("名字　%s 年龄 %d" % info_tuple)
info_str = "名字　%s 年龄 %d" % info_tuple
print(info_str)