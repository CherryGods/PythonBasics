def print_info(name, gender=True):  # 应该以最常用的值作为默认值，这里假设男生多，所以默认值为男生
    """
    打印信息
    :param name:　姓名
    :param gender:　性别:True为男生，False为女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


print_info("小明")
print_info("小美", False)
