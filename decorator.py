import time


def get_time():
    return time.time()


def time_slow(threshold):
    def wrapped_func(f):
        start = get_time()
        result=f()
        stop = get_time()
        if threshold and stop - start > threshold:
            return "Threshold exceeded: {0}".format(stop - start)

        print("{0} executed in {1}".format(f.__name__, stop - start))
        return result
    return wrapped_func


@time_slow(threshold=5)
def test_slow():
    for i in range(0, 1000000000):
        pass
