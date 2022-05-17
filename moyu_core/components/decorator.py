
import time

def runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print('运行时间 runtime :', time.time() - start_time)
        return result
    return wrapper