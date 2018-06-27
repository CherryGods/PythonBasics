def test(num, *num_args, **num_kwargs):
    print(num, num_args, num_kwargs)


test(1, (1, 2, 3), {"num": 1, "num2": 2})
