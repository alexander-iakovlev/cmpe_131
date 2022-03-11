def doubler(func):
    def test(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return test