import time
from functools import wraps
import unittest

def get_time():
    return time.time()


def time_slow(threshold):
    def wrapped_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = get_time()
            result = f(*args, **kwargs)
            stop = get_time()
            time_delta = stop - start
            if threshold and time_delta > threshold:
                return "Threshold exceeded: {0}".format(time_delta)
            print("{0} executed in {1}".format(f.__name__, time_delta))
            return result
        return wrapper
    return wrapped_func


@time_slow(threshold=20)
def test_slow(max_range):
    for i in range(max_range):
        pass
    return True


class TestDecorator(unittest.TestCase):
    def test_fast_function(self):
        self.assertTrue(test_slow(10))

    def test_slow_function(self):
        self.assertIn("Threshold exceeded: ",test_slow(1000000000))


