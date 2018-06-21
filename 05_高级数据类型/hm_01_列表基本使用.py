name_list = ["zhangsan", "lisi", "wangwu"]
# 1.取值和取索引
# list index out of range -列表超出索引范围（列表越界）
# print(name_list[3])
print(name_list[0])
# 知道数据的内容，想确定数据在列表中的位置
# 如果传递的值为列表中不存在的值，则会报错 ValueError: "object" is not in list
# print(name_list.index("zhangsan123"))
print(name_list.index("zhangsan"))
# 2.修改
# 列表指定的索引超出范围 IndexError: list assignment index out of range
# name_list[3] = "Hello"
name_list[0] = "李四"
# 3.增加
# append-在列表的末尾追加数据
name_list.append("CherryGods")
# insert-在列表所指定的索引位置前插入一个数据
name_list.insert(1, "码农")
# extend-在列表的末尾追加一个列表的所有数据
temp_list = ["苹果", "橡胶", "葡萄", "玫瑰花"]
name_list.extend(temp_list)
# 4.删除
# remove-在列表中删除指定的数据
name_list.remove("lisi")
# pop-未传递参数时删除列表中末尾的数据
name_list.pop()
# pop-删除指定索引的数据
name_list.pop(2)
# clear-清空所有数据
name_list.clear()
print(name_list)
