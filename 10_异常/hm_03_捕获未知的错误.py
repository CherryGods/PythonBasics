# 提示用户输入一个整数
try:
    num = int(input("请输入一个整数:"))
    result = 10 / num
    print(result)
except ValueError:
    print("必须输入整数!")
# except ZeroDivisionError:
#     print("不能输入0作为被除数!")
# 捕捉未知的错误
except Exception as result:
    print("未知错误　%s" % result)
