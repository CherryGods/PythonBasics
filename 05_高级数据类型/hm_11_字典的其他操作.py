cherrygods = {"name": "cherrygods",
              "age": 16}
# 统计键值对数量
print(len(cherrygods))

# 合并字典
temp_dict = {"love:": "MineCraft"}
# 如果被合并的字典的键和要合并的字典中的键有重复，那么被合并的字典的键值对则会则会被覆盖
cherrygods.update(temp_dict)

# 输出字典中的所有值
print(cherrygods.values())

# 以键值对的形式将字典输出
print(cherrygods.items())

# 返回一个新的字典，具有可迭代的值和值相等的值
print(cherrygods.fromkeys("cherrygods"))

# 输出字典中的所有key
print(cherrygods.keys())

# 清空字典
temp_dict.clear()
print(temp_dict)
print(cherrygods)
