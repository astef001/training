import collections
import unittest


def check_immutable(obj):
    mutable_list = [list, dict, set]
    if type(obj) in mutable_list:
        return False
    if isinstance(obj, collections.Iterable):
        for elem in obj:
            if not check_immutable(elem):
                return False
    return True


def swap(arg):
    result = {}

    for k, v in arg.items():
        if not check_immutable(v):
            return False
        else:
            if collections.Counter(list(arg.values()))[v] != 1:
                return False
            result[v] = k
    return result


class TestSwap(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(swap({}), {})

    def test_mutable_key(self):
        self.assertEqual(swap({'a': (1, 2, [3])}), False)

    def test_simple_dict(self):
        self.assertEqual(swap({'a': 123, 'b': 456}), {123: 'a', 456: 'b'})

    def test_nested_tuples(self):
        self.assertEqual(swap({'a': (1, (2, (3, {'b': 4})))}), False)

    def test_duplicate_key(self):
        self.assertEqual(swap({'a': 123, 'b': 456, 'c': 123}), False)