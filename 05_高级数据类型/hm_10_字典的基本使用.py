cherrygods = {"name": "cherrygods"}

# 取值
print(cherrygods["name"])
# 在取值的时候如果所指定的key不存在，则会报错
# print(cherrygods["name2"])
# 增加
cherrygods["age"] = 18
# 修改
# 若key存在修改，若不存在则新增
cherrygods["name"] = "CherryGods"
# 删除
# 指定要删除的key
cherrygods.pop("name")
# 在删除指定键值对队的时候，如果key不存在则会报错
cherrygods.pop("name2")
print(cherrygods)
