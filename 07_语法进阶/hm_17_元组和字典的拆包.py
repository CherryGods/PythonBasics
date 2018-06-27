def test(*args, **kwargs):
    print(args)
    print(kwargs)


gl_tuple = (1, 2, 3, 4, 5, 6, 7)
gl_dict = {"name": "CherryGods", "age": 16}
# 未拆包
# test(gl_tuple, gl_dict)
# 拆包后
test(*gl_tuple, **gl_dict)
