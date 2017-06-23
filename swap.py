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
            print("Swap is not possible")
            return False
        else:
            if collections.Counter(arg.values())[v] > 1:
                print("Swap is not possible")
                return False
            result[v] = k

    return result


class TestSwap(unittest.TestCase):
    def testEmptyDict(self):
        self.assertEqual(swap({}), {})

    def testMutableKey(self):
        self.assertEqual(swap({'a': (1, 2, [3])}), False)

    def testDuplicateValue(self):
        self.assertEqual(swap({'a': 123, 'b': 456, 'c': 123}), False)

    def testSimpleDict(self):
        self.assertEqual(swap({'a': 123, 'b': 456}), {123: 'a', 456: 'b'})
