import time
from functools import wraps

def get_time():
    return time.time()


def time_slow(threshold):
    def wrapped_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = get_time()
            result = f(*args, **kwargs)
            stop = get_time()
            if threshold and stop - start > threshold:
                return "Threshold exceeded: {0}".format(stop - start)
            print("{0} executed in {1}".format(f.__name__, stop - start))
            return result
        return wrapper
    return wrapped_func


@time_slow(threshold=22)
def test_slow():
    for i in range(0, 1000000000):
        pass

print(test_slow)