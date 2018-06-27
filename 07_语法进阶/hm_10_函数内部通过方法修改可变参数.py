def test01(name_list):
    print("函数内部的代码")
    name_list.append(9)
    print(name_list)
    print("函数执行完成")


gl_name_list = [1, 2, 3]
test01(gl_name_list)
print(gl_name_list)
