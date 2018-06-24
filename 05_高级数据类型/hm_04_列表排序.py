str_list = ['a', 'c', 'b', 'd']
num_list = [4, 3, 2, 1]
# 无变化
print("无变化:")
print(str_list)
print(num_list)
# # 升序
print("升序:")
str_list.sort()
num_list.sort()

print(str_list)
print(num_list)
# # 降序
print("降序:")
str_list.sort(reverse=True)
num_list.sort(reverse=True)

print(str_list)
print(num_list)

# 逆序（反转）
print("逆序（反转）:")
str_list.reverse()
num_list.reverse()
print(str_list)

