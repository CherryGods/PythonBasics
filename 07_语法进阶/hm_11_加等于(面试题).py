def test01(num, num_list):
    print("函数开始执行")
    num += num
    # 本质上列表变量在做+=操作时相当于调用extend方法，所以数据会发生变化
    # num_list += num_list
    num_list.extend(num_list)
    print(num)
    print(num_list)
    print("函数执行完成")


gl_num_list = [1, 2, 3]
gl_num = 10
test01(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)
