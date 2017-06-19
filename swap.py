import collections
import unittest


def check_immutable(obj):
    mutable_list = [list, dict, set]
    if type(obj) in mutable_list:
        return False
    if isinstance(obj, collections.Iterable):
        for elem in obj:
            if type(elem) in mutable_list:
                return False
    return True


def swap(arg):
    result = {}
    for k, v in arg.items():
        if not check_immutable(v):
            return "Swap is not possible"
        else:
            result[v] = k

    return result


class TestSwap(unittest.TestCase):
    def testEmptyDict(self):
        self.assertEqual(swap({}), {})

    def testMutableKey(self):
        self.assertEqual(swap({'a': (1, 2, [3])}), "Swap is not possible")

    def testSimpleDict(self):
        self.assertEqual(swap({'a': 123, 'b': 456}), {123: 'a', 456: 'b'})
