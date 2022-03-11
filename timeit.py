import time

def calculate_time(func):
    def test(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("Total time ", end_time - start_time)
    return test