import time


class TimeSlow(object):
    @staticmethod
    def get_time():
        return time.time()

    def __init__(self, threshold):
        self.threshold = threshold

    def __call__(self, f):
        def wrapped_f():
            start = self.get_time()
            f()
            stop = self.get_time()
            if self.threshold and stop - start > self.threshold:
                print("Threshold exceeded: {0}".format(stop-start))
            else:
                print("{0} executed in {1}".format(f.__name__, stop-start))
        return wrapped_f


@TimeSlow(threshold=21)
def test_slow():
    for i in range(0, 1000000000):
        pass
