def test01():
    name = "CherryGods"
    age = 16
    # 返回一个元组
    return name, age


print(test01()[0], test01()[1], type(test01()))
# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 那么可以定义多个变量去接收一个函数的返回值
# 注意，如果使用多个变量接收元组返回值时，需要跟元组元素的数量保持一致
gl_name, gl_age = test01()

print(gl_name, gl_age)
