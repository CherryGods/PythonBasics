# 尝试执行的代码
try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数:"))
    result = 10 / num
    print(result)
# 捕获到某个异常时执行的代码
except ValueError:
    print("必须输入整数!")
except ZeroDivisionError:
    print("不能输入0作为被除数!")
# 代码顺利执行后要执行的代码
else:
    print("代码执行成功")
# 无论代码是否成功执行都会执行的代码
finally:
    print("无论是否成功都会执行的代码")
