def func_counter(func):
    def test(*args, **kwargs):
        test.counter += 1
        return func(*args, **kwargs)

    test.counter = 0
    return test